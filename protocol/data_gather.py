import abc
import time
import socket
import datetime
import json
import traceback

filepath = 'profile.json'
with open(filepath, 'r') as f:
    try:
        response = json.load(f)
    except Exception as e:
        print(traceback.format_exc())

ip_addr = response['target_ip']
port_number = int(response['target_port'])

class DataGather(object):
    
    def __init__(self, ip, port):
        self.ip = ip_addr
        self.port = port_number
        self.client = None
        self.buffer = None

    def check_init_frame(self):
        pass

    def devide_header(self):
        pass




if __name__ == "__main__":
    pass