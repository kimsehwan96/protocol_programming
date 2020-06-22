import threading
import time
import traceback
import datetime

count = 0

def thread_run():
    print("function executed ! {}".format(datetime.datetime.now()))
    global count
    count += 1
    print(count)
    t = threading.Timer(5, thread_run)
    t.start()
    if count > 5:
        t.cancel()
        count = 0

if __name__ == "__main__":
    thread_run()
        
