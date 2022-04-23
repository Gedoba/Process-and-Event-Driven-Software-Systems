import requests
import time
import numpy as np

class Measurement:
    def __init__(self, time_filename, measurement_filename):
        self.time_filename = time_filename
        self.measurement_filename = measurement_filename
        self.read_file()

    def read_file(self):
        self.time = np.genfromtxt(self.time_filename, delimiter=',', dtype="str")
        self.measurement = np.genfromtxt(self.measurement_filename, delimiter=',', dtype="float")

    def send_data(self):
        time_start = 80000 # 8.00
        start_tick = 95
        for i in range(start_tick, len(self.measurement[0])):
            data = {'value': int(self.measurement[0][i] * 1000), 'time': time_start}
            requests.post('http://localhost:8089/cgmMeasurements', json=data)
            time_start += 500
            time.sleep(2)
        

measurement = Measurement('time.csv', 'measurements.csv')
measurement.send_data()