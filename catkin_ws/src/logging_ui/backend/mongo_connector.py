from pymongo import MongoClient, timeout as pymongo_timeout
from alpaca_logging_tools import metadata_dataclasses
from alpaca_logging_tools.metadata_dataclasses import ros_master_uri_regex, ros_ip_regex, topic_regex
import regex as re
default_topics_list = (
'/arm/1/joint_states',
'/arm/1/wrench',
'/sensor/camera/1/color/camera_info',
'/sensor/camera/1/color/image_raw',
'/sensor/camera/1/depth/camera_info',
'/sensor/camera/1/depth/image_rect_raw',
'/sensor/camera/1/depth/color/points',
'/sensor/camera/1/aligned_depth_to_color/camera_info',
'/sensor/camera/1/aligned_depth_to_color/image_raw'
)
class MongoConnector:
    def __init__(self, host, port, db_name, login, password):
        uri = f"mongodb://{login}:{password}@{host}:{port}"
        self._client = MongoClient(uri, serverSelectionTimeoutMS=1000)
        self._db = self._client[db_name]
        self._db.command("ping")

    def get_ros_connection_config(self):
        
        ros_connection_config = self._db['ros_connection_config'].find_one()
        if ros_connection_config is None:
            self.set_ros_connection_config()
        ros_connection_config = self._db['ros_connection_config'].find_one()
        ros_connection_config.pop('_id')
        return ros_connection_config

    def set_ros_connection_config(self, ros_master_uri="http://127.0.0.1:11311", ros_ip="127.0.0.1"):
        if not re.match(ros_master_uri_regex, ros_master_uri):
            raise ValueError("ROS Master URI is invalid, please use the format http://<ip>:<port>")
        if not re.match(ros_ip_regex, ros_ip):
            raise ValueError("ROS IP is invalid, please use the format <ip>")
        ros_connection_config = self._db['ros_connection_config'].find_one()
        if ros_connection_config is None:
            ros_connection_config = {"ros_master_uri": ros_master_uri, 
                                    "ros_ip": ros_ip}
            self._db['ros_connection_config'].insert_one(ros_connection_config)
        else:
            self._db['ros_connection_config'].update_one({}, {"$set": {"ros_master_uri": ros_master_uri, 
                                    "ros_ip": ros_ip}})
        
    def get_topics_list(self):
        topics_list = self._db['topics_list'].find_one()
        if topics_list is None:
            self.set_topics_list()
        topics_list = self._db['topics_list'].find_one()
        topics_list.pop('_id')
        return topics_list['topics_list']
    
    def set_topics_list(self, topics_list=None):
        if topics_list is None:
            topics_list = list(default_topics_list)
        topics_list = list(filter(lambda x: re.match(topic_regex, x), topics_list))
        if self._db['topics_list'].find_one() is None:
            self._db['topics_list'].insert_one({"topics_list": topics_list})
        else:
            self._db['topics_list'].update_one({}, {"$set": {"topics_list": topics_list}})
            
    def get_metadata(self) -> metadata_dataclasses.MetaData_0_1_static:
        metadata = self._db['metadata'].find_one()
        if metadata is None:
            self.set_metadata()
        metadata = self._db['metadata'].find_one()
        metadata.pop('_id')
        return metadata

    def set_metadata(self, metadata: metadata_dataclasses.MetaData_0_1_static=None) -> None:
        if metadata is None:
            metadata = metadata_dataclasses.MetaData_0_1_static(**{
            'source_type': 'internal',
            'source': 'Unknown',
            'team': 'Unknown',
            'version_of_requirements': "0.1",
            'dataset_types': 'IM',
            'method_collection': 'teleop',
            'repository_link': 'gitflic.ru/repo',
            'branch_name': 'LLM-dev',
            'commit_hash': 'Unknown',
            'agents_weight_link': "hf.com",
            'language_of_instruction': 'rus+eng',
            'robot_type': 'UR5',
            'gripper_type': 'WSG-50',
            'robot_configuration': 'semantic_description.urdf',
            'teleop_device': 'joystick',
            'planner_weight_link': '',
            'planned_subtasks': '',
            'scenario_task': '',
        })
        if self._db['metadata'].find_one() is None:
            self._db['metadata'].insert_one(metadata.model_dump())
        else:
            self._db['metadata'].update_one({}, {"$set": metadata.model_dump()})

    def set_last_record(self, date, time, episode_id):
        data = {"date": date, "time": time, "episode_id": episode_id}
        if self._db['last_record'].find_one() is None:
            self._db['last_record'].insert_one(data)
        else:
            self._db['last_record'].update_one({}, {"$set": data})

    def get_last_record(self):
        last_record = self._db['last_record'].find_one()
        if last_record is None:
            return {'date': '2023-07-19',
                    'time': '09-28-31',
                    'episode_id': 0}
        last_record.pop('_id')
        last_record['episode_id'] = int(last_record['episode_id'])
        return last_record
        