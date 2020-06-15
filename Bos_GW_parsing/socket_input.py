import os
import json
from socket import *
from datetime import datetime
from time import sleep
from struct import pack, unpack

# default Bosch gateway's sampling time = 100ms
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
  "period": 1000 # 100ms
}

TEST_BUFF = {
    'brake': [29.0, 30, 40], 
    'valve': [10, 20, 30], 
    'pressure': [1, 2, 3], 
    'tempreature': [1, 1, 1]
    }

fields = TEST_DATA_SOURCE['payload'].get("fields")
sampling_time = TEST_DATA_SOURCE.get("period")

def init_buffer(fields: list): #input fields list
    BUFF = {}
    for i in fields:
        BUFF[i] = []
    return BUFF

# sending binary data as [brake_value, pressure_value, temperature_value, valve_value]
def convert_data(user_data, data):
    fmt = user_data['payload']['format']
    return pack(fmt, *data)

def split_data(byte_data: bytes):
    decoded_data = byte_data.decode('utf-8')
    split_data = decoded_data.split('\n')
    processed_list = split_data[:-1:]
    return processed_list

def vaildate_data(byte_data: bytes):
    if byte_data.decode('utf-8')[-1::] != '\n':
        return False
    else:
        return True

def parsing_data(list_data: list, buf: dict):
    for i in list_data:
        dict_data = json.loads(i)
        #print("this is dict_data{}".format(dict_data))
        field = list(dict_data.keys())[0]
        #print("this is field {}".format(field))
        #print("this is buf {}".format(buf))
        buf[field].append(dict_data[field])
    #print("parsed dict {}".format(buf))
    return buf

def latest_data(stored_buffer: dict, fields: list):
    latest_list = []
    for i in fields:
        try:
            latest_list.append(stored_buffer.get(i)[-1])
        except IndexError as e: #when first few ms in this code runs, PR21 Doesn't send all of fields datas so we need to wait few ms
            latest_list.append(None)
    stored_buffer = init_buffer(fields) # reset buffer
    print("this is latest_data{} : time stamp {}".format(latest_list, datetime.now()))
    return latest_list
#TODO: making latest_data function to get latest data in dictionary

def recv_msg(host: str, port: int, fields: list):
    print("this is fields {}".format(fields))
    buf = init_buffer(fields)
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(1)
    connectionSock, addr = sock.accept() #inital connection printing
    print(str(addr), "address")
    while True:
        data = connectionSock.recv(65536)
        while vaildate_data(data) == False:
            data += connectionSock.recv(65536)
        result = split_data(data)
        #print(result)
        #print("-"*50)
        stored_buf = parsing_data(result, buf) #dictionary return
        sleep(sampling_time/1000)
        latest_data(stored_buf, fields) # this is actual pushing data

        #TODO: 데이터를 수집한 이후 dict 데이터를 주기적으로 clear 할 필요가 있음.
        # 그렇지 않으면 메모리 누수 발생함. 
        # 주기적으로 init_buffer를 하는게 맞을듯.

if __name__ == "__main__":
    print(init_buffer(fields))
    buff = init_buffer(fields)
    recv_msg('', 55065, fields)

    