from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QModelIndex
import typing
import pydantic
from ui_py import logging_ui
from application_modules.backend_connector import BackendNotConnectedException
from application_modules.ros_configuration_window import ROSConfiguration
from application_modules.metadata_configuration_window import MetadataConfiguration
import requests
import datetime
import time
from alpaca_logging_tools import metadata_dataclasses as metadata_typing
import logging
version_of_requirements = "0.1"

class MainWindowClass(QMainWindow, logging_ui.Ui_MainWindow):
    def __init__(self, backend_connector, rosbag_srv_addr, parent=None, main_window=None):
        self._logger = logging.getLogger("logging_ui.main_window")
        self._bc = backend_connector
        tries = 5
        for i in range(tries):
            if self._bc.ping():
                break
            time.sleep(1)
        else:
            self.show_error_message(header="Backend is not running", message=f"Backend is not running on {self._bc.backend_url}.<br>Tried {tries} times to connect.")
            exit(1)
        super(MainWindowClass, self).__init__(parent)
        self._rosbag_srv_addr = rosbag_srv_addr
        self.setupUi(main_window)
        self.instruction_source.addItems(["supervised", "dataset", 'open-source', 'LLM'])
        self._set_episode_id()
        self._connect_triggers()
    
    def _connect_triggers(self):
        self.actionconnection.triggered.connect(self.ros_communication_dialog)
        self.actionmetadata.triggered.connect(self.metadata_dialog)
        self.start_button.mousePressEvent = lambda event: self.episode_start_button_clicked()
        self.stop_button.mousePressEvent = lambda event: self.episode_stop_button_clicked()
        self.save_button.mousePressEvent = lambda event: self.save_button_clicked()
        self.discard_button.mousePressEvent = lambda event: self.discard_button_clicked()

    def ros_communication_dialog(self):
        self.dialog = QMainWindow()
        self.ui = ROSConfiguration(backend_connector=self._bc, main_window=self.dialog)
        self.dialog.show()
    
    def metadata_dialog(self):
        self.dialog = QMainWindow()
        self.ui = MetadataConfiguration(self._bc, main_window=self.dialog)
        self.dialog.show()
    
    def episode_button_clicked(self, button_id):
        set_enabled = (self.start_button.setEnabled, self.stop_button.setEnabled, self.save_button.setEnabled, self.discard_button.setEnabled)
        state = {
            0: (False, True, False, False),
            1: (False, False, True, True),
            2: (True, False, False, False),
            3: (True, False, False, False)
        }[button_id]
        for i, enabled in enumerate(state):
            set_enabled[i](enabled)
    
    def episode_start_button_clicked(self):
        self.start_button.setEnabled(False)
        self.episode_id.setEnabled(False)
        self.subtask_id.setEnabled(False)
        self.repaint()
        try:
            static_metadata = self._bc.get_metadata()
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            self.episode_button_clicked(3)
            return
        try:
            dynamic_metadata = self._collect_dynamic_metadata_start()
            compiled_metadata = {**static_metadata, **dynamic_metadata.model_dump()}
            metadata = metadata_typing.MetaData_0_1(**compiled_metadata)
        except pydantic.ValidationError as e:
            self.show_error_message(header = "data is invalid", message = str(e.json()))
            self.episode_button_clicked(3)
            return
        try:
            topics_list = self._bc.get_topics_list()
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            self.episode_button_clicked(3)
            return
        body = {
            "topics_list": topics_list,
            "metadata": metadata.model_dump()
        }
        try:
            resp = requests.post(f"{self._rosbag_srv_addr}/record", params={"version": static_metadata["version_of_requirements"]}, json=body)
        except Exception as e:
            self._logger.exception(e)
            self.show_error_message(str(e))
            self.episode_button_clicked(3)
            return
        else:
            if resp.status_code == 422:
                self.show_error_message(header = "data is invalid", message = resp.text)
                self.episode_button_clicked(3)
                return
            elif resp.status_code != 200:
                self.show_error_message(resp.text)
                self.episode_button_clicked(3)
                return
            self.episode_succeeded.setEnabled(True)
        self.episode_button_clicked(0)
        self._show_record_start_info_message(metadata, topics_list)

    def _collect_dynamic_metadata_start(self) -> metadata_typing.MetaData_0_1_dynamic:
        global version_of_requirements
        scenario_id = int(self.episode_id.text())
        subtask_id = int(self.subtask_id.text())
        success_of_tasks = 0
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H-%M-%S")
        timestamp_start = int(time.time_ns())
        timestamp_end = int(time.time_ns())
        current_instruction = self.current_instruction.toPlainText()
        planned_subtasks = self.planned_subtasks.toPlainText()
        scenario_task = self.scenario_task.toPlainText()
        instruction_source = self.instruction_source.currentText()
        return metadata_typing.MetaData_0_1_dynamic(date=date,
                                                    time=current_time,
                                                    timestamp_start=timestamp_start,
                                                    timestamp_end=timestamp_end,
                                                    scenario_id=scenario_id,
                                                    subtask_id=subtask_id,
                                                    version_of_requirements=version_of_requirements,
                                                    current_instruction=current_instruction,
                                                    planned_subtasks=planned_subtasks,
                                                    scenario_task=scenario_task,
                                                    instruction_source=instruction_source,
                                                    success_of_tasks=success_of_tasks)
    
    def _collect_dynamic_metadata_stop(self) -> dict:
        success_of_tasks = 1 if self.episode_succeeded.isChecked() else 0
        timestamp_end = int(time.time_ns())
        current_instruction = self.current_instruction.toPlainText()
        planned_subtasks = self.planned_subtasks.toPlainText()
        scenario_task = self.scenario_task.toPlainText()
        instruction_source = self.instruction_source.currentText()
        return {"success_of_tasks": success_of_tasks, 
                "timestamp_end": timestamp_end,
                "current_instruction": current_instruction,
                "planned_subtasks": planned_subtasks,
                "scenario_task": scenario_task,
                "instruction_source": instruction_source}

    def episode_stop_button_clicked(self):
        data = self._collect_dynamic_metadata_stop()
        self.episode_succeeded.setEnabled(False)
        self.stop_button.setEnabled(False)
        try:
            resp = requests.post(f"{self._rosbag_srv_addr}/stop", json=data)
        except Exception as e:
            self._logger.exception(e)
            self.show_error_message(str(e))
            return
        else:
            if resp.status_code != 200:
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}")
                return
            if resp.text != "OK":
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}", header="Warning")
        self.episode_succeeded.setChecked(False)
        self.episode_button_clicked(1)

        # TODO: stop episode

    def save_button_clicked(self):
        # QSpinBox returns string
        try:
            resp = requests.post(f"{self._rosbag_srv_addr}/save")
        except Exception as e:
            self._logger.exception(e)
            self.show_error_message(str(e))
            return
        else:
            if resp.status_code != 200:
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}")
                return
            if resp.text != "OK":
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}", header="Warning")
        current_episode_id = int(self.episode_id.text())
        self._logger.info(f"current_episode_id: {current_episode_id}")
        try:
            self._bc.save_last_record({'date': datetime.datetime.now().strftime("%Y-%m-%d"), 
                                       'time': datetime.datetime.now().strftime("%H-%M-%S"),
                                       'episode_id': current_episode_id})
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
        _last_subtask_id = self.subtask_id.text()
        self._set_episode_id()
        self.show_info_message(header="Episode saved", message=f"""Episode <b>{current_episode_id}</b>, 
subtask <b>{_last_subtask_id}</b> saved successfully<br>Next episode id: {current_episode_id + 1}<br>Next subtask id: 1""")
        self.episode_button_clicked(2)
        # TODO: save episode

    def discard_button_clicked(self):
        try:
            resp = requests.post(f"{self._rosbag_srv_addr}/discard")
        except Exception as e:
            self._logger.exception(e)
            self.show_error_message(str(e))
            return
        else:
            if resp.status_code != 200:
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}")
                return
            if resp.text != "OK":
                self.show_error_message(f"Code: {resp.status_code}\nmessage: {resp.text}", header="Warning")
        self.episode_button_clicked(3)
        # TODO: discard episode

    def show_error_message(self, message, header="Error"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(header)
        msg.exec_()
    
    def show_info_message(self, message, header="Info"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(header)
        msg.exec_()
    
    def _set_episode_id(self):
        try:
            last_record = self._bc.get_last_record()
        except BackendNotConnectedException as e:
            self.episode_id.setValue(1)
            self.subtask_id.setValue(1)
            self.show_error_message(str(e))
            return
        last_date = last_record["date"]
        last_date_obj = datetime.datetime.strptime(last_date, "%Y-%m-%d")
        if last_date_obj.date() == datetime.datetime.now().date():
            self.episode_id.setValue(last_record["episode_id"] + 1)
            self.subtask_id.setValue(1)
        else:
            self.episode_id.setValue(1)
            self.subtask_id.setValue(1)

    def _show_record_start_info_message(self, metadata, topics_list):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        metadata_message = "<br>".join([f"<b>{key}:</b> {value}" for key, value in metadata.model_dump().items()])
        topics_list = "<br>".join(f"<b>-</b> {topic}" for topic in topics_list)
        message_string = f"<i>Recording started with metadata:</i><br>{metadata_message}<br><br><i>Topics:</i><br>{topics_list}"
        msg.setText(message_string)
        msg.setWindowTitle("Recording started")
        msg.exec_()
    
    def rosbag_srv_callback(self, status):
        if not status["rosbag_srv_is_running"]:
            for button_obj in (self.start_button, self.stop_button, self.save_button, self.discard_button):
                button_obj.setEnabled(False)
            self.rosbag_srv_status.setText("Rosbag_srv is not running")
            self.episode_id.setEnabled(False)
            self.subtask_id.setEnabled(False)
            self.episode_succeeded.setEnabled(False)
            self.roscore_status.setPixmap(QtGui.QPixmap("resources/cross.png"))
            self.ros_connected_label.setText("ROS Master status: Unknown")
            self.current_filename.setText("Current filename: None")
            return
        self.current_filename.setText(f"Current filename: {status['filename']}")
        if status["roscore_is_running"]:
            self.ros_connected_label.setText("ROS Master is running")
            self.roscore_status.setPixmap(QtGui.QPixmap("resources/check.png"))
        else:
            self.ros_connected_label.setText("ROS Master is not running")
            self.roscore_status.setPixmap(QtGui.QPixmap("resources/cross.png"))
        if status["is_recording"]:
            self.episode_button_clicked(0)
            self.episode_id.setEnabled(False)
            self.subtask_id.setEnabled(False)
            self.episode_succeeded.setEnabled(True)
            self.rosbag_srv_status.setText(f"Logging episode")
        else:
            self.episode_succeeded.setEnabled(False)
            self.episode_succeeded.setChecked(False)
            if status["filename"]:
                self.episode_id.setEnabled(False)
                self.subtask_id.setEnabled(False)
                self.episode_button_clicked(1)
                # TODO: save episode
            else:
                if status['roscore_is_running']:
                    self.episode_button_clicked(3)
                    self.episode_id.setEnabled(True)
                    self.subtask_id.setEnabled(True)
                    self.rosbag_srv_status.setText("Logging stopped, please start new episode")
                else:
                    for button_obj in (self.start_button, self.stop_button, self.save_button, self.discard_button):
                        button_obj.setEnabled(False)
                    self.episode_id.setEnabled(False)
                    self.subtask_id.setEnabled(False)
                    self.episode_succeeded.setEnabled(False)
                    self.rosbag_srv_status.setText("ROS Master is not running, please check ROS connection settings")
