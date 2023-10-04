#!/usr/bin/env python3

import sys
import os
import logging
import signal
import time
from PyQt5.QtWidgets import QMainWindow, QApplication
from application_modules.backend_connector import BackendConnector, BackendNotConnectedException
from application_modules.ros_service_monitor import ROSBagSrvMonitor
from application_modules.ros_configuration_window import ROSConfiguration
from application_modules.metadata_configuration_window import MetadataConfiguration
from application_modules.main_window import MainWindowClass

def terminate(signal, frame):
    logging.info("terminating")
    # rosbag_monitor.stop()
    main_ui.close()
    sys.exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    signal.signal(signal.SIGTERM, terminate)
    app = QApplication(sys.argv)
    backend_connector = BackendConnector()
    backend_port = os.environ.get("GUI_BACKEND_PORT", 8012)
    backend_connector.backend_url = f"http://0.0.0.0:{backend_port}"
    rosbag_srv_port = os.environ.get("ROSBAG_SRV_PORT", 8011)
    rosbag_srv_url = f"http://0.0.0.0:{rosbag_srv_port}"
    rosbag_monitor = ROSBagSrvMonitor(backend_connector, rosbag_srv_url, delay=0.5)
    rosbag_monitor.start()
    main_window = QMainWindow()
    main_ui = MainWindowClass(backend_connector,
                                rosbag_srv_addr=rosbag_srv_url,
                                parent=None, 
                                main_window=main_window)
    
    rosbag_monitor.callback = main_ui.rosbag_srv_callback
    main_window.show()
    sys.exit(app.exec_())
