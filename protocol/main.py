import threading
import time
import traceback
import datetime
from protocol.data_manager import DataFramer
from protocol.data_manager import Command
from protocol.data_manager import DataGather



count = 0
data_gather = DataGather('127.0.0.1', 9999)

def thread_run():   
    global count
    count += 1

    print(count)
    print("function executed ! {}".format(datetime.datetime.now()))

    oper = data_gather.get_operands()
    data_gather.factory(oper).do() #factory design
    
    t = threading.Timer(5, thread_run)
    t.start()
    if count > 5:
        t.cancel()
        count = 0

if __name__ == "__main__":
    thread_run()
        
