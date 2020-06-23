import threading
import time
import traceback
import datetime
from data_manager import DataFramer
from data_manager import Command
from data_manager import DataGather
from revolution_pi import TestPi
from _thread import start_new_thread #메인스레드가 돌고 있을 때 새로운 서비스 요청이 들어오면

# 새로운 스레드를 실행해서 프로세스를 처리한다 / 이 프로세스 처리 완료 될 때 까지 나머지 프로세스는
# 펜딩 되어야 한다 -> 펜딩 되면 안되는 스레드도 있다 // 데이터 게더링 <- 이건 계속 프로세스가 돌고 있어야 함
# -> 소켓을 감시하고 있다가, 특정 명령어가 들어오면 / 스레드를 실행하고 (1회성 처리),
# 프로세스가 끝나면 exit으로 종료시키자.
# 소켓을 감시하는 스레드(절대 죽지 않고, 커넥션 끊어지면 리커넥션 맺는)를 작성해서, 
# 메인 스레드와 소켓 감시 스레드를 동시에 돌리고, 소켓 감시 스레드는 항상 버퍼를 쌓아둔다.
# 버퍼에서 메인스레드가 데이터를 꺼내와서 명령어에 맞게 분기시키기.

data_gather = DataGather('127.0.0.1', 9999)
pi = TestPi()


def thread_run():   
    print("function executed ! {}".format(datetime.datetime.now()))
    oper = data_gather.get_operands()
    data_gather.factory(oper).do() #factory design
    t = threading.Timer(5, thread_run)
    t.start()

    #TODO: 5분마다 TDAT 로직 run, 
    # 새로운 명령어가 들어올 경우 해당 명령어 처리.
def get_port_data():
    pi.get_current_data()
    print("data gathered from pi {}".format(datetime.datetime.now()))
    t2 = threading.Timer(1, get_port_data)
    t2.start()

if __name__ == "__main__":
    get_port_data()
    thread_run()
        
