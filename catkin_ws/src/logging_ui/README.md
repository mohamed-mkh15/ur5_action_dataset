# ROS Bag UI
This repository contains tools for collecting datasets using ROS Bag files

# Table of Contents
- [Structure](#structure)
- [Installation](#installation)
- - [Requirements](#requirements)
- - [Building](#building)
- [Running](#running)
- - [Setting up environment](#setting-up-environment)
- - [Running all the services](#running-all-the-services)
- [Usage](#usage)
- - [Recording](#recording)


# Structure
This project is divided into three parts:
- [ROS connector](/alpaca_logging_tools/), which is submodule of this repository and could be used as standalone package
- [backend service](/backend) which is MongoDB connector 
- [frontend UI](/main.py) which is Qt application and could be used in docker container or directly on host machine

# Installation
## Requirements
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Qt5](https://doc.qt.io/qt-5/gettingstarted.html)
- [PyQt5](https://pypi.org/project/PyQt5/)
## Building
Qt5 application is pre-built and could be run as is, but if you want to edit UI you should build it by yourself using following commands:
```bash
pyuic5 logging.ui -o ui_py/logging_ui.py
pyuic5 ros_communication_settings.ui -o ui_py/ros_communication_settings_ui.py
pyuic5 metadata.ui -o ui_py/metadata_ui.py
```
# Running
## Setting up environment
Before running the UI you should set up environment variables:
```bash
export SAVED_ROS_BAGS_PATH=/path/to/ros/bags # here you should specify path to directory where you want to save ROS bags
```
Also, if it is needed, you can specify services ports at [.env file](/docker/.env)
## Running all the services
Navigate to the docker directory and run the following command:
```bash
xhost +local:root # allow root user to access X server
docker compose -f docker-compose.yml up --build
```
It will pull MongoDB image and build backend service and run all the services in docker containers.
# Usage
## Recording
After running all the services you should see the following window:
![Main window](/_docs/main_window.png)
If you see ***ROS Master is not running*** message, you should run ROS Master set up ros connection settings at *preferencesー>ros communication* tab and press *Save* button. If it doesn't help, you should check if ROS Master is running and ROS Environment variables are set up correctly. 
After that you should see the following window:
![Main window](/_docs/main_window_started.png)
***Note:*** remember to configure your own metadata and topics-to-record list before starting recording.  
When recording is stopped you may select ***instruction-source*** and edit ***scenrio task***, ***planned subtasks*** and ***current instruction*** fields.
When recording started you are able to set ***episode succeeded*** flag
If recording was interrupted by ROS Master shutdown or stopped manually, you won't be able to edit any fields.  
After recording is finished you must save or discard current record. If you discard it by mistake, you can find it in volume accessing inside docker container *rosbag_service* at cache directory.
```bash
docker exec -ti rosbag bash -c "cd /root/.cache/rosbag && bash"
```
***Note:*** don't forget to clean cache directory from time to time, because it could take a lot of space.
## Using ROS Bag service as standalone package
You can use ROS Bag service as standalone package dirctly from your python code. Firt of all you should add it to your python path:
```dockerfile
ENV PYTHONPATH "${PYTHONPATH}:/workspace/alpaca_logging_tools/"
```
Then run it as ros node:
```bash
rosrun alpaca_logging_tools rosbag_log_service.py
```
In your code you can use it as follows:
```python
import time
from alpaca_logging_tools import ROSBagLoggerConnector, DynamicMetaDataDataclass
if __name__ == '__main__':
    rosbag_logger = ROSBagLoggerConnector('http://0.0.0.0:8011',
                                            source_type='internal',
                                            source='Company',
                                            team='Pepe',
                                            version_of_requirements='0.1',
                                            dataset_types='IM',
                                            method_collection='agent',
                                            teleop_device='joystick',
                                            repository_link='',
                                            branch_name='develop',
                                            commit_hash='',
                                            agents_weight_link='',
                                            language_of_instruction='eng',
                                            instruction_source='LLM',
                                            planner_weight_link='',
                                            robot_type='UR5',
                                            gripper_type='WSG-50',
                                            robot_configuration='')
    topics_list = ['/arm/1/joint_states', ]
    test_dict = {
        'scenario_id': 1,
        'subtask_id': 1,
        'success_of_tasks': 0,
        'scenario_task': "Как открыть окно? Даны следующие yes элементы: окно, домашний офис. Окно находится в домашнем офисе. Окно закрыто.",
        'planned_subtasks': 'Пройдите в домашний офис. Подойти к yes окну. Открыть окно.',
        'current_instruction': '',
    }
    with rosbag_logger.log_rosbag(DynamicMetaDataDataclass(**test_dict), topics_list) as (response, done_req):
        time.sleep(2)
        done_req.update({
            'success_of_tasks': 1,
            'current_instruction': 'Пройдите в домашний офис.'
        })
```
