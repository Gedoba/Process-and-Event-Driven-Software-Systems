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
        self.measurement = np.genfromtxt(self.measurement_filename, delimiter=',', dtype="str")

    def send_data(self):
        for i in range(len(self.time)):
            data = {'value': self.measurement[0][i], 'time': self.time[i]}
            requests.post('http://localhost:8082/cgmMeasurements', json=data)
            time.sleep(5)
        

measurement = Measurement('time.csv', 'measurements.csv')
measurement.send_data()