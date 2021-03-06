import revpimodio2
import traceback
import json
import random

filepath = 'profile.json'
IMGPATH = '/dev/picontrol0'

class RevolutionPi:

    def __init__(self, profile_json):
        self.data_ports = []
        with open(filepath, 'r') as f:
            try:
                self.profile = json.load(f)
            except Exception as e:
                print(traceback.format_exc())
        self.port_names = self.profile['revpi_portnames']
        self.revolution_pi = revpimodio2.RevPiModIO(autorefresh = True, procimg = IMGPATH)
        self.IO = self.revolution_pi.io
        self.data_length = len(self.port_names)
        self.data = []
        for idx in range(self.data_length):
            self.data.append(0)

    def get_current_data(self):
        for idx in range(self.data_length):
            self.data[idx] = getattr(self.IO, self.port_names).value

        return self.data #list will return [value, value, value, value]
        #revolution pi's data will return.


class TestPi:
    def __init__(self):
        pass

    def get_current_data(self):
        a = random.randint(1, 1000)
        b = random.randint(5,50)
        c = random.randint(60, 1000)
        print([a,b,c])
        return [a, b, c]
        