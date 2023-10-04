from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QMainWindow
import re
from ui_py import ros_communication_settings_ui
from application_modules.backend_connector import BackendNotConnectedException
import logging

ros_master_uri_regex = r"^http://(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$"
ros_ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
topic_regex = r"^\/[a-zA-Z0-9_\/]+$"
class ROSConfiguration(QMainWindow, ros_communication_settings_ui.Ui_MainWindow):
    class TopicsListModel(QtCore.QAbstractListModel):
        def __init__(self, parent=None):
            self._logger = logging.getLogger("ros_communication_settings_window.topics_list_model")
            QtCore.QAbstractListModel.__init__(self, parent)
            self._topics = ["<new item>"]
            self.dataChanged.connect(self.data_changed_emit)

        def data(self, index, role):
            if role == QtCore.Qt.DisplayRole:
                row = index.row()
                value = self._topics[row]
                return value
            
        def rowCount(self, index):
            return len(self._topics)
        
        def setData(self, index, value, role):
            if role == QtCore.Qt.EditRole:
                if not re.match(topic_regex, value):
                    return False
                self._topics[index.row()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        
        def flags(self, index):
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable 
        
        @property
        def topics(self):
            ret = list(filter(lambda x: x and x != "<new item>", self._topics))
            return ret
        
        @topics.setter
        def topics(self, value):
            value = list(filter(lambda x: x and x != "<new item>", value))
            self._topics = value
            self.dataChanged.emit(self.index(0, 0), self.index(len(self._topics), 0))
        
        def removeRows(self, row, count, parent=QModelIndex()):
            self.beginRemoveRows(parent, row, row + count - 1)
            del self._topics[row:row + count]
            self.endRemoveRows()
            return True
        
        def remove_selected_item(self, event):
            if event.key() == QtCore.Qt.Key_Delete:
                selected_rows = self.parent().selectionModel().selectedRows()
                if len(selected_rows) > 0:
                    self.removeRows(selected_rows[0].row(), len(selected_rows))
    
        def data_changed_emit(self, *args, **kwargs):
            self._topics = list(filter(lambda x: x and x != "<new item>", self._topics))
            self._topics = list(filter(lambda x: re.match(topic_regex, x), self._topics))
            self._topics = list(set(self._topics))
            self._topics.sort()
            self._topics.append("<new item>")

        def topics_list_context_menu(self, pos):
            menu = QtWidgets.QMenu()
            menu.addAction("Copy selected", self.copy_selected)
            menu.addAction("Add from clipboard", self.add_from_clipboard)
            menu.addAction("Remove selected", self.remove_selected)
            menu.exec_(QtGui.QCursor.pos())
        
        def remove_selected(self):
            selected_rows = self.parent().selectionModel().selectedRows()
            if len(selected_rows) > 0:
                self.removeRows(selected_rows[0].row(), len(selected_rows))
                self.dataChanged.emit(self.index(0, 0), self.index(len(self._topics), 0))

        def copy_selected(self):
            selected_rows = self.parent().selectionModel().selectedRows()
            if len(selected_rows) > 0:
                topic = list(map(lambda x: self._topics[x.row()], selected_rows))
                topic = list(filter(lambda x: x and x != "<new item>", topic))
                topic = "\n".join(topic)
                QtWidgets.QApplication.clipboard().setText(topic)
        
        def add_from_clipboard(self):
            topics = QtWidgets.QApplication.clipboard().text()
            # split by new line or space
            topics = re.split(r"\n|\s", topics)
            topics = list(filter(lambda x: re.match(topic_regex, x), topics))
            self._topics.extend(topics)
            self.dataChanged.emit(self.index(0, 0), self.index(len(self._topics), 0))


    def __init__(self, backend_connector, parent=None, main_window=None):
        self._logger = logging.getLogger("ros_communication_settings_window")
        super(ROSConfiguration, self).__init__(parent)
        self._bc = backend_connector
        self.setupUi(main_window)
        try:
            self.refresh()
        except RuntimeError as e:
            self.close()
            raise e
        self.save_config_settings.accepted.connect(self.save_config_settings_clicked)
        self.save_config_settings.rejected.connect(self._fill_config)
        self.save_topics_settings.accepted.connect(self.save_topics_settings_clicked)
        self.save_topics_settings.rejected.connect(self._fill_topics_list)
        self.ros_ip.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(ros_ip_regex)))
        self.ros_master_uri.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(ros_master_uri_regex)))        

    def refresh(self):
        self._fill_config()
        self._fill_topics_list()
    
    def _fill_topics_list(self):
        try:
            # topics = self._bc.get_topics()
            topics = self._bc.get_topics_list()
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            self.save_topics_settings.setEnabled(False)
            return
        self.topics_list_model = ROSConfiguration.TopicsListModel(self.topics_list)
        self.topics_list_model.topics = topics
        self.topics_list.setModel(self.topics_list_model)
        self.topics_list.selectionModel().select(self.topics_list_model.index(0, 0), QtCore.QItemSelectionModel.Select)
        self.topics_list.setAlternatingRowColors(True)
        self.topics_list.keyPressEvent = self.topics_list_model.remove_selected_item
        self.topics_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.topics_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.topics_list.customContextMenuRequested.connect(self.topics_list_model.topics_list_context_menu)
        self.save_topics_settings.setEnabled(True)

    def save_topics_settings_clicked(self):
        topics = self.topics_list_model.topics
        try:
            self._bc.save_topics_list(topics)
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            return
        else:
            self.refresh()    
    
    def _fill_config(self):
        try:
            ros_connection_config = self._bc.get_ros_connection_config()
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            self.save_config_settings.setEnabled(False)
            return
        ros_master_uri = ros_connection_config["ros_master_uri"]
        ros_ip = ros_connection_config["ros_ip"]
        self.ros_master_uri.setText(ros_master_uri)
        self.ros_ip.setText(ros_ip)
        self.save_config_settings.setEnabled(True)

    def save_config_settings_clicked(self):
        ros_ip = self.ros_ip.text()
        ros_master_uri = self.ros_master_uri.text()
        if not re.match(ros_ip_regex, ros_ip):
            self.show_error_message("ROS IP is invalid")
            return
        if not re.match(ros_master_uri_regex, ros_master_uri):
            self.show_error_message("ROS Master URI is invalid")
            return
        try:
            self._bc.save_ros_connection_config(ros_master_uri, ros_ip)
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            return
    
    def show_error_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
