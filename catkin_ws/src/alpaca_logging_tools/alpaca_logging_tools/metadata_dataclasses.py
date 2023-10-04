from pydantic import BaseModel, validator, constr
import logging
from datetime import date, time, datetime
from typing import Any, Literal, List
import pandas as pd

ros_master_uri_regex = r"^http://(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$"
ros_ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
topic_regex = r"^\/[a-zA-Z0-9_\/]+$"
class MetaDataBaseStatic(BaseModel):
    team: str
    version_of_requirements: str

    @validator("version_of_requirements")
    def _check_version(cls, value):
        current_version = cls._version_of_requirements.get_default()
        if value != current_version:
            raise ValueError(f"Version of requirements is {value}, but current version is {current_version}")
        return value

class MetaDataBaseDynamic(BaseModel):
    date: str
    time: str
    timestamp_start: int
    timestamp_end: int
    scenario_id: int
    subtask_id: int
    version_of_requirements: str
    rosbag_name: str = 'unknown'

    @validator("version_of_requirements")
    def _check_version(cls, value):
        current_version = cls._version_of_requirements.get_default()
        if value != current_version:
            raise ValueError(f"Version of requirements is {value}, but current version is {current_version}")
        return value

    @validator("time", pre=True)
    def _parse_time(cls, value):
        return datetime.strptime(value, '%H-%M-%S').time().strftime('%H-%M-%S')
    
    @validator("date", pre=True)
    def _parse_date(cls, value):
        return datetime.strptime(value, '%Y-%m-%d').date().strftime('%Y-%m-%d')

    def to_pandas(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict([self.model_dump()])
    
    def to_parquet(self, **kwargs):
        return self.to_pandas().to_parquet(**kwargs)
    
class MetaData_0_1_static(MetaDataBaseStatic):
    _version_of_requirements: str = '0.1'

    source_type: Literal['external', 'open-source', 'internal']
    source: str
    dataset_types:  constr(pattern=r"^[IMN]*$", to_upper=True, min_length=1, max_length=3)
    method_collection: str
    teleop_device: str = None
    repository_link: str
    branch_name: str
    commit_hash: str
    agents_weight_link: str
    language_of_instruction: Literal['rus', 'eng', 'rus+eng']
    planner_weight_link: str = None
    robot_type: str
    gripper_type: str
    robot_configuration: str
    
    @validator("dataset_types")
    def _validate_dataset_types(cls, value):
        assert len(value) == len(set(value)), f"dataset_types should not contain duplicates, but it contains {value}"
        return value

class MetaData_0_1_dynamic(MetaDataBaseDynamic):
    _version_of_requirements: str = '0.1'

    current_instruction: str
    instruction_source: str
    success_of_tasks: int
    planned_subtasks: str = None
    scenario_task: str = None

    @validator("success_of_tasks")
    def _validate_int_bool(cls, value):
        assert value in (0, 1), f'success_of_tasks should be 0 or 1, not "{value}"'
        return value

class MetaData_0_1(MetaData_0_1_static, MetaData_0_1_dynamic):
    _version_of_requirements: str = '0.1'

    def __init__(self, **data):
        super().__init__(**data)
        self.rosbag_name = f'team={self.team}_scenario_id={self.scenario_id}_subtask_id={self.subtask_id}_date={self.timestamp_start}.bag'
    

version2class = {
    "0.1": MetaData_0_1
}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_dict = {
        'date': '2023-07-19',
        'time': '09-28-31',
        'timestamp_start': '1690881855',
        'timestamp_end': '1690881966',
        'scenario_id': 1,
        'subtask_id': 1,
        'source_type': 'internal',
        'source': 'sber',
        'team': 'Федотова',
        'version_of_requirements': 0.1,
        'dataset_types': 'INM',
        'method_collection': 'agent',
        'repository_link': 'git.sberrobots.ru/repo',
        'branch_name': 'LLM-dev',
        'commit_hash': 'aijdpjkas12123adfs',
        'agents_weight_link': "hf.com",
        'scenario_task': "Как открыть окно? Даны следующие yes элементы: окно, домашний офис. Окно находится в домашнем офисе. Окно закрыто.",
        'planned_subtasks': 'Пройдите в домашний офис. Подойти к yes окну. Открыть окно.',
        'language_of_instruction': 'rus+eng',
        'current_instruction': 'Пройдите в домашний офис.',
        'instruction_source': 'LLM',
        'planner_weight_link': 'hf.com',
        'success_of_tasks': 1,
        'robot_type': 'UR5',
        'gripper_type': 'WSG-50',
        'robot_configuration': 'semantic_descr.urdf',

    }
    metadata = MetaData_0_1(**test_dict)
    metadata.to_parquet(path="file.parquet", engine='auto', compression='snappy', index=None, partition_cols=None, storage_options=None)