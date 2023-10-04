import requests
import logging

class BackendNotConnectedException(Exception):
    pass

def is_connected_to_backend_wrapper(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.ping():
            try:
                ret = func(*args, **kwargs)
            except requests.exceptions.ConnectionError as e:
                raise BackendNotConnectedException(f'Cannot connect to backend at: "{self.backend_url}"')
        else:
            raise BackendNotConnectedException(f'Cannot connect to backend at: "{self.backend_url}"')
        return ret
    return wrapper

class BackendConnector:
    def __init__(self):
        self._logger = logging.getLogger("backend_connector")
        self._backend_url = None
    
    @property
    def backend_url(self):
        return self._backend_url
    
    @backend_url.setter
    def backend_url(self, value):
        self._backend_url = value

    def ping(self):
        if self.backend_url is None:
            return False
        try:
            response = requests.get(self.backend_url)
            if response.status_code == 200:
                return True
        except:
            return False
    
    @is_connected_to_backend_wrapper
    def get_metadata(self):
        response = requests.get(self.backend_url + "/metadata")
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def get_ros_connection_config(self):
        response = requests.get(self.backend_url + "/get_ros_connection_config")
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def save_ros_connection_config(self, ros_master_uri, ros_ip):
        response = requests.post(self.backend_url + "/set_ros_connection_config", params={"ros_master_uri": ros_master_uri, "ros_ip": ros_ip})
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def save_metadata(self, metadata) -> requests.Response:
        response = requests.post(self.backend_url + "/set_metadata", json=metadata)
        return response
    
    @is_connected_to_backend_wrapper
    def get_metadata(self):
        response = requests.get(self.backend_url + "/get_metadata")
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def get_topics_list(self):
        response = requests.get(self.backend_url + "/get_topics_list")
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def save_topics_list(self, topics):
        data = {"topics_list": topics}
        response = requests.post(self.backend_url + "/set_topics_list", json=data)
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def get_last_record(self):
        response = requests.get(self.backend_url + "/get_last_record")
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()
    
    @is_connected_to_backend_wrapper
    def save_last_record(self, last_record):
        response = requests.post(self.backend_url + "/set_last_record", json=last_record)
        if response.status_code != 200:
            raise BackendNotConnectedException(f'Error code: "{response.status_code}", text: "{response.text}"')
        return response.json()