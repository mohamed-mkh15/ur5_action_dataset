#! /usr/bin/env python3

from copy import deepcopy
import json

import pydantic
import rospy, rosgraph
import rosbag
from std_msgs.msg import String
import pandas as pd
from flask import Flask, request
from alpaca_logging_tools import version2class
from threading import Thread, Lock
import logging
import subprocess
from time import sleep
from pathlib import Path
import os, signal
import regex as re
import shutil

ros_master_uri_regex = r"^http://(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$"
ros_ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

# def fix_logging(level=logging.INFO):
#     console = logging.StreamHandler()
#     console.setLevel(level)
#     logging.getLogger('').addHandler(console)
#     formatter = logging.Formatter('%(levelname)-8s:%(name)-12s: %(message)s')
#     console.setFormatter(formatter)
#     logging.getLogger('').addHandler(console)

class Logger:
    # using custom logger because ROS environment replaces original logger with its own
    # not using ROS logger because it is not available when roscore is down 
    def __init__(self, name):
        self._name = name
        self.info = lambda message: self._print_message('INFO', message)
        self.warning = lambda message: self._print_message('WARNING', message)
        self.error = lambda message: self._print_message('ERROR', message)
        self.critical = lambda message: self._print_message('CRITICAL', message)
        self.debug = lambda message: self._print_message('DEBUG', message)

    def _print_message(self, level, message):
        print(f'{level}:{self._name}: {message}')

class RESTApp:
    def __init__(self, port, ros_connector, rosbag_path="/root/.cache/rosbag/", save_path="/root/.cache/rosbag_saves"):
        self._logger = Logger("rest_app")
        self._app = Flask(__name__)
        self._port = port
        self._rosbag_path = Path(rosbag_path)
        self._rosbag_path.mkdir(parents=True, exist_ok=True)
        self._save_path = Path(save_path)
        self._save_path.mkdir(parents=True, exist_ok=True)
        self._ros_connector = ros_connector
        self._ros_connector.trigger_roscore_not_running = self._ros_is_down
        self._configure_endpoints()
        self._process = None
        self._current_filename = ""
        self._current_metadata = None
        self._save_lock = Lock()

    def _ros_is_down(self):
        if self.is_recording:
            self._logger.warning('roscore is down, killing rosbag recorder process...')
            try:
                self._stop_current_record()
            except Exception as e:
                self._logger.warning(f'error stopping current record: {e}')

    def _configure_endpoints(self):
        self._app.add_url_rule("/record", methods=["GET", "POST"], view_func=self.start_record)
        self._app.add_url_rule("/stop", methods=["GET", "POST"], view_func=self.stop_record)
        self._app.add_url_rule("/save", methods=["GET", "POST"], view_func=self.save_record)
        self._app.add_url_rule("/discard", methods=["GET", "POST"], view_func=self.discard_record)
        self._app.add_url_rule("/status", methods=["GET", "POST"], view_func=self.status)
        self._app.add_url_rule("/update_ros_connection_config", methods=["GET", "POST"], view_func=self.update_ros_connection_config)

    def status(self):
        return {"is_recording": self.is_recording,
                "filename": self._current_filename,
                "roscore_is_running": self._ros_connector.is_roscore_running,
                "ROS_MASTER_URI": self._ros_connector._ROS_MASTER_URI,
                "ROS_IP": self._ros_connector._ROS_IP,
                }, 200

    def update_ros_connection_config(self):
        self._logger.info(f"updare connection config request: {request.json}")
        try:
            ROS_MASTER_URI = str(request.json['ROS_MASTER_URI'])
            ROS_IP = str(request.json['ROS_IP'])
        except KeyError:
            return '"ROS_MASTER_URI" and "ROS_IP" parameters required', 400
        try:
            self._ros_connector.update_ros_connection_config(ROS_MASTER_URI, ROS_IP)
        except ValueError as e:
            return str(e), 400
        else:
            return "OK", 200

    def start_record(self):
        self._logger.info(f"start record request: {request.args}")
        try:
            version = str(request.args['version'])
        except KeyError:
            return '"version" parameter required', 400
        try:
            MetaData = version2class[version]
        except KeyError:
            return f'version "{version}" not found from: {version2class.keys()}', 400
        try:
            metadata_dict = request.get_json()['metadata']
            topics_list = request.get_json()['topics_list']
            metadata = MetaData(**metadata_dict)
        except pydantic.ValidationError as e:
            return str(e), 422
        except KeyError as e:
            return f'KeyError: {str(e)}', 400
        else:
            try:
                self._run_rosbag(metadata.rosbag_name, metadata, topics_list)
            except RuntimeError as e:
                return str(e), 400
            return "OK", 200
    
    def _sigkill(self):
        if self.is_recording:
            self._process.terminate()
            self._process.wait()
            self._process = None

    @property
    def is_recording(self):
        return isinstance(self._process, subprocess.Popen)

    def stop_record(self):
        self._logger.info(f"stop record request: {request.json}")
        if not self.is_recording and not self._current_filename:
            return "not recording", 405
        elif not self.is_recording and self._current_filename:
            return "record already stopped, but not saved", 405
        metadata_dict = self._current_metadata.model_dump()
        if request.headers.get('Content-Type') == 'application/json':
            self._logger.info(f'updating metadata with new values: {request.get_json()}')
            metadata_dict.update(**request.get_json())
        try:
            metadata = type(self._current_metadata)(**metadata_dict)
        except pydantic.ValidationError as e:
            self._logger.warning(f'recording not stopped because of invalid metadata: {e}')
            return str(e), 422
        else:
            self._current_metadata = metadata
            try:
                self._stop_current_record()
            except Exception as e:
                return str(e), 400
        return 'OK', 200

    def save_record(self):
        if self.is_recording:
            return "record is running, stop it first", 405
        if not self._current_filename:
            return "no record to save", 405
        current_path = Path(self._rosbag_path / self._current_filename)
        target_path = Path(self._save_path / self._current_filename)
        try:
            self._move_record(current_path, target_path)
        except Exception as e:
            return str(e), 400
        try:
            _csv_path = self._add_row_into_csv()
            # raise RuntimeError(f'csv_path: {csv_path}')
        except Exception as e:
            return str(e), 400
        self._current_filename = ""
        self._current_metadata = None
        return "OK", 200
        
    def _add_row_into_csv(self):
        rosbag_path = Path(self._save_path / self._current_filename).parent
        csv_path = Path(rosbag_path / f"team={self._current_metadata.team}_episode_id={self._current_metadata.scenario_id}.csv")
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        if not csv_path.exists():
            pd.DataFrame(columns=list(self._current_metadata.dict().keys())).to_csv(csv_path, index=False)
        df = pd.read_csv(csv_path)
        df = pd.concat([df, self._current_metadata.to_pandas()], ignore_index=True)
        df.to_csv(csv_path, index=False)
        return csv_path
        
    def discard_record(self):
        if self.is_recording:
            return "record is running, stop it first", 405
        if not self._current_filename:
            return "no record to discard", 405
        self._current_filename = ""
        self._current_metadata = None
        return "OK", 200
        
    def _move_record(self, current_location, target_location):
        # move file to correct location
        self._logger.info(f'moving file from "{current_location}" to "{target_location}"')
        try:
            target_location = Path(target_location)
            target_location.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(current_location, target_location)
        except Exception as e:
            self._logger.warning(f'error moving file: {e}')
            raise RuntimeError(f'error moving file: {e}')
        else:
            self._logger.info(f'file moved to "{target_location}"')
            return True

    def _stop_current_record(self):
        if not self.is_recording:
            return
        self._sigkill()
        self._write_metadata()
        
    def run(self):
        self._flask_thread = Thread(target=self._app.run, daemon=True, name="FlaskThread", args=(), kwargs={"host": "0.0.0.0", "port": self._port})  
        self._flask_thread.start()
    
    def _write_metadata(self):
        filename = self._current_filename
        metadata = self._current_metadata
        metadata_string = json.dumps(metadata.model_dump(), indent=4, ensure_ascii=False)
        self._logger.info(f'writing metadata to: "{filename}"\nmetadata:\n{metadata_string}')
        file_path = self._rosbag_path / filename
        for try_n in range(5):
            try:
                with rosbag.Bag(file_path, 'a') as bag:
                    metadata_msg = String(data=metadata_string)
                    try:
                        time = bag.get_end_time()
                    except rosbag.bag.ROSBagException:
                        self._logger.warning(f'error getting end time, setting to 0')
                        time = 0
                    bag.write('/metadata', metadata_msg, rospy.Time(time))
            except rosbag.bag.ROSBagException as e:
                self._logger.warning(f'try {try_n + 1}/5: error writing metadata: {e}')
            else:
                self._logger.info(f'metadata written to: {filename}')
                break
        else:
            raise RuntimeError(f'error writing metadata to: {filename}')

    def _run_rosbag(self, filename, metadata, topics_to_record):
        if self.is_recording:
            self._logger.warning('rosbag run called before stop recording, killing rosbag recorder process...')
            try:
                self._stop_current_record()
            except Exception as e:
                self._logger.warning(f'error stopping current record: {e}')
        sub_path = Path(f"{metadata.team}/{metadata.robot_configuration}/{metadata.date}/")
        rosbag_sub_path = self._rosbag_path / sub_path
        rosbag_sub_path.mkdir(parents=True, exist_ok=True)
        file_path = rosbag_sub_path / filename
        output_name = str(file_path)
        cmd = ['rosbag', 'record', f'--output-name={output_name}', *topics_to_record]
        cmd_str = " ".join(cmd)
        self._logger.info(f'executing command: "{cmd_str}"')
        if not self._ros_connector.is_roscore_running:
            self._logger.error('roscore is not running, exiting...')
            raise RuntimeError('roscore is not running')
        self._process = subprocess.Popen(cmd,
                                        shell=False)
        self._logger.info(f'started rosbag with pid: "{self._process.pid}"')
        self._current_filename = str(sub_path / filename)
        self._current_metadata = metadata
    
    def stop(self):
        self._process and self._process.terminate()
        self._process and self._process.wait()
        self._process = None
        self._flask_thread and self._flask_thread.join()
        self._flask_thread = None

class ROSConnector:
    def __init__(self, ROS_MASTER_URI="http://127.0.0.1:11311", ROS_IP="127.0.0.1"):
        self._logger = Logger("ros_state_monitor")
        self.update_ros_connection_config(ROS_MASTER_URI, ROS_IP)
        self._roscore_checker_lock = Lock()
        self._rosgraph_monitor_thread = None
        self._trigger_roscore_not_running = None
        self._running = True

    def _rosgraph_monitor(self):
        while self._running:
            state = self._is_roscore_running()
            if self._trigger_roscore_not_running:
                (not state) and self._trigger_roscore_not_running()

    def _is_roscore_running(self):
        with self._roscore_checker_lock:
            try:
                return rosgraph.is_master_online()
            except Exception as e:
                return False
        
    @property
    def is_roscore_running(self):
        return self._is_roscore_running()
    
    @property
    def trigger_roscore_not_running(self):
        return self._trigger_roscore_not_running

    @trigger_roscore_not_running.setter
    def trigger_roscore_not_running(self, callback:callable):
        self._logger.info('trigger on "roscore is not running" set')
        self._trigger_roscore_not_running = callback

    def update_ros_connection_config(self, ROS_MASTER_URI, ROS_IP):
        if not re.match(ros_master_uri_regex, ROS_MASTER_URI):
            raise ValueError("ROS Master URI is invalid, please use the format http://<ip>:<port>")
        if not re.match(ros_ip_regex, ROS_IP):
            raise ValueError("ROS IP is invalid, please use the format <ip>")
        
        self._ROS_MASTER_URI = ROS_MASTER_URI
        self._ROS_IP = ROS_IP
        os.environ['ROS_MASTER_URI'] = ROS_MASTER_URI
        os.environ['ROS_IP'] = ROS_IP

    def run(self):
        self._rosgraph_monitor_thread = Thread(target=self._rosgraph_monitor, daemon=True, name="ROSGraphMonitorThread", args=(), kwargs={})
        self._rosgraph_monitor_thread.start()

    def stop(self):
        self._running = False
        self._rosgraph_monitor_thread and self._rosgraph_monitor_thread.join()
        self._rosgraph_monitor_thread = None

def terminate(signal, frame):
    rest_app.stop()
    ros_connector.stop()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, terminate)
    signal.signal(signal.SIGTERM, terminate)
    ros_connector = ROSConnector()
    ros_connector.run()
    # fix_logging()
    # logging.basicConfig(level=logging.INFO)
    rest_app = RESTApp(port=os.environ.get('ROSBAG_SRV_PORT', 8011),
                    ros_connector=ros_connector,
                    rosbag_path= "/root/.cache/rosbag/",
                    save_path= "/root/saved_rosbags")
    rest_app.run()
    rest_app._flask_thread.join()