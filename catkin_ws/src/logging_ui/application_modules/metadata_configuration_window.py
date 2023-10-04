from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QModelIndex
import typing
from ui_py import metadata_ui
from application_modules.backend_connector import BackendNotConnectedException
import logging

class MetadataConfiguration(QMainWindow, metadata_ui.Ui_Metadata):
    class MetadataTableModel(QtCore.QAbstractTableModel):
        def __init__(self, data:dict, parent=None):
            self._logger = logging.getLogger("metadata_configuration_window.table_model")
            QtCore.QAbstractTableModel.__init__(self, parent)
            self._pos_to_key = lambda pos: list(self._data.keys())[pos]
            self._data = {key: {"value": value, "show_name": key, "updated_value": value} for key, value in data.items()}
            self.columnCount = lambda parent: 3
            

        def headerData(self, section, orientation, role):
            if role == QtCore.Qt.DisplayRole:
                if orientation == QtCore.Qt.Horizontal:
                    return ["value", "prev value", "is edited"][section]
                elif orientation == QtCore.Qt.Vertical:
                    return self._data[self._pos_to_key(section)]["show_name"]
            return None

        def rowCount(self, parent):
            return len(self._data)
        
        def data(self, index, role):
            if role == QtCore.Qt.DisplayRole:
                if index.column() == 0:
                    return self._data[self._pos_to_key(index.row())]["updated_value"]
                elif index.column() == 1:
                    return self._data[self._pos_to_key(index.row())]["value"]
                elif index.column() == 2:
                    return "✗" if self._data[self._pos_to_key(index.row())]["value"] != \
                        self._data[self._pos_to_key(index.row())]["updated_value"] else ""
                
            return None

        def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
            if value:
                self._data[self._pos_to_key(index.row())]["updated_value"] = value
            return super().setData(index, value, role)
            
        def flags(self, index):
            return  (QtCore.Qt.ItemIsEnabled if index.column() in (0, ) else 0)| QtCore.Qt.ItemIsSelectable | \
                (QtCore.Qt.ItemIsEditable if index.column() == 0 else 0)
        
        def get_data(self):
            return {key: value["updated_value"] for key, value in self._data.items()}

    def __init__(self, backend_connector, parent=None, main_window=None):
        self._logger = logging.getLogger("metadata_configuration_window")
        super(MetadataConfiguration, self).__init__(parent)
        self._bc = backend_connector
        self.setupUi(main_window)
        try:
            self.refresh()
        except RuntimeError as e:
            self.close()
            raise e
        self.save_settings.accepted.connect(self.save_settings_clicked)
        self.save_settings.rejected.connect(self.refresh)
        
    def refresh(self):
        try:
            metadata_config = self._bc.get_metadata()
            self.tableView.setModel(self.MetadataTableModel(metadata_config))
            self.tableView.setAlternatingRowColors(True)
            self.tableView.resizeRowsToContents()
            self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            self.tableView.verticalHeader().setMaximumWidth(200)
            self.tableView.verticalHeader().setMinimumWidth(200)
            self.tableView.verticalHeader().setDefaultSectionSize(30)
            self.tableView.setColumnWidth(0, 400)
            self.tableView.setColumnWidth(1, 400)
            self.tableView.setColumnWidth(2, 95)
            self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            self.tableView.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
            self.tableView.clicked.connect(lambda index: QtWidgets.QApplication.clipboard().setText(index.data()) if index.column() == 1 else None)
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            raise RuntimeError(str(e))
    
    def save_settings_clicked(self):
        try:
            metadata_config = self.tableView.model().get_data()
            resp = self._bc.save_metadata(metadata_config)
            if resp.status_code == 422:
                self._logger.error(resp.json())
                error_description = "\n".join([f"<b>{error['loc'][1]}:</b> {error['msg']}" for error in resp.json()["detail"]])
                self.show_error_message(header = "data is invalid", message = error_description)
            elif resp.status_code == 200:
                self.refresh()
            else:
                self.show_error_message(header = "unknown error", message = resp.text)
                
        except BackendNotConnectedException as e:
            self.show_error_message(str(e))
            return
    
    def show_error_message(self, message, header="Error"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(header)
        msg.exec_()