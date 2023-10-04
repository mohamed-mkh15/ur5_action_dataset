from threading import Thread, Lock
import time
import requests
from application_modules.backend_connector import BackendNotConnectedException
import logging

class ROSBagSrvMonitor:
    def __init__(self, backend_connector, host, delay=1):
        self._logger = logging.getLogger("rosbag_srv_monitor")
        self._bc = backend_connector
        self._host = host
        self._status_monitoring_thread = None
        self._ros_config_monitoring_thread = None
        self._callback = None
        self._delay = delay
        self._lock = Lock()
        self._status = None
        self._ros_config = None
        self._loop = True

    def _rosbag_srv_requestor(self):
        while self._loop:
            status = self._get_status()
            try:
                if status is None:
                    self._logger.warning("error during rosbag_srv status request")
                    self._callback and self._callback({"rosbag_srv_is_running": False,
                                                        "roscore_is_running": False, 
                                                        "is_recording": False, 
                                                        "filename": None})
                else:
                    self._callback and self._callback({ "rosbag_srv_is_running": True,
                                                    "roscore_is_running": status["roscore_is_running"], 
                                                    "is_recording": status["is_recording"], 
                                                "filename": status["filename"]})
            except BackendNotConnectedException as e:
                self._logger.error(f"failed to get rosbag_srv status because backend is not available")
            except Exception as e:
                self._logger.exception(f"error during rosbag_srv status callback: {e}")
            time.sleep(self._delay)

    def _rosbag_srv_config_updater(self):
        while self._loop:
            ros_config = self._get_ros_config()
            ros_srv_status = self._get_status()
            if ros_config and ros_srv_status:
                if ros_config['ROS_MASTER_URI'] != ros_srv_status['ROS_MASTER_URI'] or \
                    ros_config['ROS_IP'] != ros_srv_status['ROS_IP']:
                    self._logger.info("updating rosbag_srv ros_config")
                    try:
                        requests.post(f"{self._host}/update_ros_connection_config", json=ros_config)
                    except requests.exceptions.ConnectionError as e:
                        self._logger.error(f"failed to update rosbag_srv ros_config: {e}")
                    except Exception as e:
                        self._logger.exception(f"error during rosbag_srv ros_config update: {e}")
            time.sleep(self._delay)

    def _get_status(self):
        with self._lock:
            try:
                response = requests.get(f"{self._host}/status")
            except requests.exceptions.ConnectionError as e:
                self._logger.error(f"failed to get rosbag_srv status because rosbag service is not available")
                return None
            except Exception as e:
                self._logger.exception(f"error during rosbag_srv status request: {e}")
                return None
            else:
                if response.status_code == 200:
                    return response.json()
                else:
                    self._logger.warning(f"status code: {response.status_code}\ntext: {response.text}")
                    return None

    def start(self):
        self._status_monitoring_thread = Thread(target=self._rosbag_srv_requestor, daemon=True, name="ROSBagServiceRequestor", args=(), kwargs={})
        self._ros_config_monitoring_thread = Thread(target=self._rosbag_srv_config_updater, daemon=True, name="ROSConfigMonitoringThread", args=(), kwargs={})
        self._status_monitoring_thread.start()
        self._ros_config_monitoring_thread.start()
        
    @property
    def callback(self):
        return self._callback
    
    @callback.setter
    def callback(self, callback):
        self._callback = callback

    @property
    def status(self):
        self._status = self._get_status()
        return self._status
    
    @property
    def ros_config(self):
        self._ros_config = self._get_ros_config()
        return self._ros_config
        
    def _get_ros_config(self):
        try:
            ros_config = self._bc.get_ros_connection_config()
        except BackendNotConnectedException as e:
            self._logger.error(f"failed to get rosbag_srv ros_config because backend is not available")
        except Exception as e:
            self._logger.exception(f"error during rosbag_srv ros_config request: {e}")
            return None
        else:
            return {"ROS_MASTER_URI": ros_config["ros_master_uri"], 
                    "ROS_IP": ros_config["ros_ip"]}
    
    def stop(self):
        self._loop = False
        self._status_monitoring_thread and self._status_monitoring_thread.join()
        self._ros_config_monitoring_thread and self._ros_config_monitoring_thread.join()
        self._status_monitoring_thread = None
        self._ros_config_monitoring_thread = None
        self._callback = None
        self._status = None
        self._ros_config = None