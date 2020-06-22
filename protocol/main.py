import threading
import time
import traceback
import datetime
from data_manager import DataGather
from command import Command, ReceiveCmd, PDUM, TDAT

count = 0
data_gather = DataGather('127.0.0.1', 9999)

def thread_run():   
    print("function executed ! {}".format(datetime.datetime.now()))
    global count
    count += 1
    print(count)
    oper = data_gather.get_operands()
    #print(" this is oper {}".format(oper))
    if data_gather.check_init_frame():
        data_gather.factory(oper).do()
        print("passed for checking init frame")
    else:
        print("faild to pass checking loigc")
    t = threading.Timer(5, thread_run)
    t.start()
    if count > 5:
        t.cancel()
        count = 0

if __name__ == "__main__":
    thread_run()
        
