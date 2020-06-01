from socket import *
from datetime import datetime
from time import sleep
import json

# default Bosch gateway's sampling time = 100ms

#ordered list.
TEST_DATA_SOURCE = {
  "id": "main_plc",
  "edgeId": "test",
  "name": "Main PLC",
  "payload": {
    "fields": [
        "brake",
        "pressure",
        "temperature",
        "valve"
    ],
    "format": "hhh",
    "preprocessedFields": [
        {
            "field": "valve",
            "inputRanges": None,
            "normalizedRanges": None,
            "decimalPoint": 2
        },
        {
            "field": "vibration",
            "inputRanges": None,
            "normalizedRanges": None,
             "decimalPoint": 1
        }
    ],
    "type": "ARRAY"
  },
  "period": 500 # 500ms
}

TEST_BUFF = {
    'brake': [29.0, 30, 40], 
    'valve': [10, 20, 30], 
    'pressure': [1, 2, 3], 
    'tempreature': [1, 1, 1]
    }



def init_buffer(fields: list): #input fields list
    BUFF = {}
    for i in fields:
        BUFF[i] = []
    return BUFF

#[ "brake", "pressure" , "temperature", "valve"
# ]

# sending binary data as [brake_value, pressure_value, temperature_value, valve_value]

def split_data(byte_data: bytes):
    decoded_data = byte_data.decode('utf-8')
    split_data = decoded_data.split('\n')
    #leng = len(split_data)
    processed_list = split_data[:-1:] #:leng]

    return processed_list

def vaildate_data(byte_data: bytes):
    if byte_data.decode('utf-8')[-1::] != '\n':
        return False
    else:
        return True
        
def recv_msg(host: str, port: int, fields: list):
    print("this is fields {}".format(fields))
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(1)
    connectionSock, addr = sock.accept() #inital connection printing.
    print(str(addr), "address")
    while True:
        data = connectionSock.recv(65536)
        #print("this is first datas :{}".format(data))
        while vaildate_data(data) == False:
        #    print("True or False splitdata {}".format(vaildate_data(data)))
            data += connectionSock.recv(65536)
        #    print("this is combine data {}".format(data))

        result = split_data(data)
        print(result)
        print("-"*50)
       


if __name__ == "__main__":
    fields = TEST_DATA_SOURCE['payload'].get("fields")
    recv_msg('', 55065, fields)

    