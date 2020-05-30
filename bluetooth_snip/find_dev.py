import os
import sys
from bluetooth import *


# 목적 mac Adderess의 devie가 있는지 체크하는 모듈
# my iPhone's bluetooth module mac address 
#TODO: 인자가 주어지면 타겟 mac address bluetooth 신호 감지 가능한지 체크, 그 외에는 주변 디바이스 체크.

def find_device(target_address):
    #target_address = sys.argv[1]
    if len(sys.argv) != 2:
        print("you should input target mac address ex) aa:aa:aa:aa:aa:aa")
    
    
    profile = {
        "target_name" : None,
        "target_address" : None,
        "port" : 1
    }
    
    #만약 lookup_names 를 True로 설정하면 - 디폴트는 False - discover_devices 의 리턴은 [(튜플),(튜플)...] 로 나오고 
    #튜플의 첫번째 인자는 mac address, 두번째 인자는 host name이 들어온다.
    #host name을 받아서 출력하기
    
    discover_option = {
        "duration" : 8,
        "flush_cache" : True,
        "lookup_names" : True,
        "lookup_class" : False,
        "device_id" : 1
    }
    
    nearby_devices = discover_devices(**discover_option)
    
    print("these are nearby devices {}".format(nearby_devices))
    
    for i, v in enumerate(nearby_devices):
        if discover_option.get("lookup_names") == True:
            _addr = v[0].decode('utf-8')
            _hostname = v[1]
        else:
            print("enable discover_option -- lookup_names")
        print("this is {} address of nearby_devices : {}".format(i, _addr))
    
        if _addr == target_address:
            profile["target_address"] = _addr
            profile["target_name"] = _hostname
        else:
            pass
        
    
    if profile.get("target_address") != None:
        print("device found. target addrres {} and target_name {}".format(profile.get("target_address"), profile["target_name"]))
        print("if loop {}".format(profile.get("target_address")))
    else:
        print("could not found target device")
        print("else loop {}".format(profile.get("target_address")))
    
    return target_address


if __name__ == "__main__":
    target_address = sys.argv[1]
    find_device(target_address)



#타겟 디바이스는 bluetooth 4.0LE -> 페어링 없이 모두가 접속 가능함. (맥 어드레스만 잘 확인하면 가능.)