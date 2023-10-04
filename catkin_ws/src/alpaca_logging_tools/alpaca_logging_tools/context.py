from dataclasses import dataclass, asdict
from pydantic import BaseModel, validator, constr
import time
from typing import Any, Literal, List
import pandas as pd
from contextlib import contextmanager
import requests
try:
    from alpaca_logging_tools.metadata_dataclasses import version2class
except ImportError:
    from metadata_dataclasses import version2class
# not using logging because ROS environment replaces original logger with its own, 
# but it doesn't work when roscore is not running


@dataclass
class DynamicMetaDataDataclass:
    scenario_id: int
    subtask_id: int
    success_of_tasks: int
    scenario_task: str
    planned_subtasks: str
    current_instruction: str
    dict = lambda self: asdict(self)

class ROSBagLoggerConnector:
    def __init__(self, rosbag_srv_addr: str,
                    source_type: Literal['internal', 'external'] = 'internal',
                    source: str = 'Sber',
                    team: str = 'Unknown',
                    version_of_requirements: str = '0.1',
                    dataset_types: str = 'IM',
                    method_collection: str = 'agent',
                    teleop_device: str = 'joystick',
                    repository_link: str = '',
                    branch_name: str = '',
                    commit_hash: str = '',
                    agents_weight_link: str = '',
                    language_of_instruction: str = 'eng',
                    instruction_source: str = 'LLM',
                    planner_weight_link: str = '',
                    robot_type: str = 'UR5',
                    gripper_type: str = 'WSG-50',
                    robot_configuration: str = '') -> None:
        self._rosbag_srv_addr = rosbag_srv_addr
        self._static_metadata = {
            'source_type': source_type,
            'source': source,
            'team': team,
            'version_of_requirements': version_of_requirements,
            'dataset_types': dataset_types,
            'method_collection': method_collection,
            'teleop_device': teleop_device,
            'repository_link': repository_link,
            'branch_name': branch_name,
            'commit_hash': commit_hash,
            'agents_weight_link': agents_weight_link,
            'language_of_instruction': language_of_instruction,
            'instruction_source': instruction_source,
            'planner_weight_link': planner_weight_link,
            'robot_type': robot_type,
            'gripper_type': gripper_type,   
            'robot_configuration': robot_configuration,
        }

    @property
    def rosbag_srv_addr(self):
        return self._rosbag_srv_addr
    
    @rosbag_srv_addr.setter
    def rosbag_srv_addr(self, value):
        self._rosbag_srv_addr = value

    @property
    def static_metadata(self):
        return self._static_metadata.copy()
    
    @static_metadata.setter
    def static_metadata(self, value):
        if self._static_metadata.keys() != value.keys():
            raise ValueError(f'ERROR: static_metadata keys must be {self._static_metadata.keys()}')

    @contextmanager
    def log_rosbag(self, metadata: DynamicMetaDataDataclass, topics_list: List[str]):
        metadata = {**self._static_metadata, **metadata.dict()}
        metadata.update(**{
            'date': time.strftime('%Y-%m-%d'),
            'time': time.strftime('%H-%M-%S'),
            'timestamp_start': time.time_ns(),
            'timestamp_end': time.time_ns(),
        })
        print(f'INFO: metadata: {metadata}')
        version = str(metadata['version_of_requirements'])
        try:
            MetaData = version2class[version]
        except KeyError:
            print(f'ERROR: version "{version}" not found from: {version2class.keys()}')
        metadata = MetaData(**metadata)
        request_body = {"metadata": metadata.model_dump(),
                        "topics_list" : topics_list}
        try:
            resp = requests.post(f'{self._rosbag_srv_addr}/record', params={'version': version}, json=request_body)
        except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout) as e:
            print(f'ERROR: rosbag_srv_addr "{self._rosbag_srv_addr}" is not available, exception:\n{e}')
            resp = requests.Response()
            resp.status_code = 500
        else:
            if resp.status_code != 200:
                print(f'ERROR: rosbag_srv_addr "{self._rosbag_srv_addr}" returned status_code: {resp.status_code}\nmesssage: {resp.text}')
        done_req = dict()
        try:
            yield resp, done_req
        finally:
            done_req.update(**{
                'timestamp_end': time.time_ns(),
            })
            try:
                resp_1 = requests.post(f'{self._rosbag_srv_addr}/stop', json=done_req)
                resp_2 = requests.post(f'{self._rosbag_srv_addr}/save', json=done_req)
            except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout) as e:
                print(f'ERROR: rosbag_srv_addr "{self._rosbag_srv_addr}" is not available, exception:\n{e}')
            else:
                for resp in [resp_1, resp_2]:
                    if resp.status_code != 200:
                        print(f'ERROR: rosbag_srv_addr "{self._rosbag_srv_addr}" returned status_code: {resp.status_code}\nmesssage: {resp.text}')

if __name__ == "__main__":
    import time
    test_dict = {
        'scenario_id': 1,
        'subtask_id': 1,
        'success_of_tasks': 0,
        'scenario_task': "Как открыть окно? Даны следующие yes элементы: окно, домашний офис. Окно находится в домашнем офисе. Окно закрыто.",
        'planned_subtasks': 'Пройдите в домашний офис. Подойти к yes окну. Открыть окно.',
        'current_instruction': '',
    }
    rosbag_logger = ROSBagLoggerConnector('http://0.0.0.0:8011',
                                            source_type='internal',
                                            source='Sber',
                                            team='Unknown',
                                            version_of_requirements='0.1',
                                            dataset_types='IM',
                                            method_collection='agent',
                                            teleop_device='joystick',
                                            repository_link='',
                                            branch_name='',
                                            commit_hash='',
                                            agents_weight_link='',
                                            language_of_instruction='eng',
                                            instruction_source='LLM',
                                            planner_weight_link='',
                                            robot_type='UR5',
                                            gripper_type='WSG-50',
                                            robot_configuration='')
    topics_list = ['/rosout',
                    '/arm/1/joint_states']
    with rosbag_logger.log_rosbag(DynamicMetaDataDataclass(**test_dict), topics_list) as (response, done_req):
        # print(f'response: {response.text}\nstatus_code: {response.status_code}')
        time.sleep(2)
        done_req.update({
            'success_of_tasks': 1,
            'current_instruction': 'Пройдите в домашний офис.'
        })
    print('done')