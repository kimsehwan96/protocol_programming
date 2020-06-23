import abc
import csv
import datetime

#TODO: 게이트웨이로부터 얻은 데이터를 5초마다 평균을 내야 한다. 그리고 5초마다의 데이터를 5분씩 잘라서 저장한다.

class DataStorer:
    def __init__(self):
        self.store_path = './data'

    def get_base_time(self):
        real_time = datetime.datetime.now()
        if real_time % 5 == 0:
            self.base_time = '{}{}{}{}'.format(real_time.year, real_time.month, real_time.hour, real_time.minute)
        else:
            pass
    
    def average(self, buffer: list):
        pass

    def csv_write(self):
        pass

    def remove_old_file(self):
        pass