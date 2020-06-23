import threading
import time
import traceback
import datetime
from data_manager import DataFramer
from data_manager import Command
from data_manager import DataGather

data_gather = DataGather('127.0.0.1', 9999)

def thread_run():   

    print("function executed ! {}".format(datetime.datetime.now()))
    oper = data_gather.get_operands()
    data_gather.factory(oper).do() #factory design
    t = threading.Timer(5, thread_run)
    t.start()

    #TODO: 5분마다 TDAT 로직 run, 
    # 새로운 명령어가 들어올 경우 해당 명령어 처리.

if __name__ == "__main__":
    thread_run()
        
