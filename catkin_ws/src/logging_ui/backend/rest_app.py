from typing import List, Dict, Union
from fastapi import FastAPI
import uvicorn
from alpaca_logging_tools import metadata_dataclasses
from alpaca_logging_tools.metadata_dataclasses import ros_master_uri_regex, ros_ip_regex

class RESTApp:
    def __init__(self, host, port, db_connector):
        self._host = host
        self._port = port
        self._db = db_connector
        self._app = FastAPI()
        self.configure_endpoints()
    
    def configure_endpoints(self):
        self._app.get("/")(self.read_root)
        self._app.get("/get_metadata")(self.read_metadata)
        self._app.post("/set_metadata")(self.save_metadata)
        self._app.get("/get_ros_connection_config")(self.read_ros_connection_config)
        self._app.post("/set_ros_connection_config")(self.save_ros_connection_config)
        self._app.get("/get_topics_list")(self.get_topics_list)
        self._app.post("/set_topics_list")(self.save_topics_list)
        self._app.get("/get_last_record")(self.get_last_record)
        self._app.post("/set_last_record")(self.save_last_record)
        
    def read_root(self):
        return f"""This is the backend of the GUI. Please use the API endpoints. 
        You can find the documentation at <a href='http://{self._host}:{self._port}/docs'>http://{self._host}:{self._port}/docs</a>""", \
        200, {"Content-Type": "text/html"}

    def read_metadata(self) -> metadata_dataclasses.MetaData_0_1_static:
        return self._db.get_metadata()
    
    def save_metadata(self, metadata: metadata_dataclasses.MetaData_0_1_static):
        try:
            self._db.set_metadata(metadata)
        except Exception as e:
            return {"error": str(e)}, 400
        return
    
    def read_ros_connection_config(self):
        data = self._db.get_ros_connection_config()
        return data
    
    def save_ros_connection_config(self, ros_master_uri, ros_ip):
        try:
            self._db.set_ros_connection_config(ros_master_uri, ros_ip)
        except ValueError as e:
            print(f"error: {e}")
            return {"error": str(e)}, 400
        return {"success": True}, 200
    
    def get_topics_list(self):
        try:
            topics = self._db.get_topics_list()
            return topics
        except Exception as e:
            print(f"error: {e}")
            return {"error": str(e)}, 400
    
    def save_topics_list(self, topics_list: Dict[str, List[str]]):
        try:
            topics_list = topics_list['topics_list']
        except KeyError:
            print(f"topics_list not found in request")
            return {"error": "topics_list not found in request"}, 400
        try:
            print(f"topics_list: {topics_list}")
            self._db.set_topics_list(topics_list)
        except Exception as e:
            print(f"error: {e}")
            return {"error": str(e)}, 400
        return {"success": True}, 200
    
    def get_last_record(self):
        try:
            last_record = self._db.get_last_record()
            print(f"last_record: {last_record}")
        except Exception as e:
            print(f"error: {e}")
            return {"error": str(e)}, 400
        return last_record
    
    def save_last_record(self, last_record: Dict[str, Union[int, str]]):
        try:
            self._db.set_last_record(date= last_record['date'],
                                    time= last_record['time'],
                                    episode_id= last_record['episode_id'])
        except Exception as e:
            print(f"error: {e}")
            return {"error": str(e)}, 400
        return {"success": True}, 200
    
    def run(self):
        uvicorn.run(self._app, host=self._host, port=self._port)
