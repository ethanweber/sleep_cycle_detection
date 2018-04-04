# this code is to interface w/ our microcontroller via serial over USB

# serial library to talk with microcontroller
import serial
import io
import threading
import time
import random

class USBCommunication:
    def __init__(self, port, baud, fake=False):
        self.port = port
        self.baud = baud
        self.connected = False
        self.serial_port = None
        self.current_reading = None
        self.thread = None
        # current_values is a dictionary for the sensors and their current readings
        self.current_values = {}

        if fake is True:
            self.start_fake_data_loop()
    def connect(self):
        serial_port = serial.Serial(port, baud, timeout=0)
        self.connect = True
    # this will start the thread that runs in the background
    def start(self):
        self.thread = threading.Thread(target=self.while_reading_loop, args=())
        self.thread.start()
    def while_reading_loop(self):
        while self.connected:
            self.current_reading = self.serial_port.readline().decode()
            self.update_latest_value()

    def start_fake_data_loop(self, delay=0.001):
        self.thread = threading.Thread(target=self.fake_loop, kwargs={'delay': delay})
        self.thread.start()
    # delay in ms
    def fake_loop(self, delay=.001):
        print("Starting fake data loop.")
        while True:
            # update fake data
            sensor1 = random.randint(0, 100)
            sensor2 = random.randint(0, 100)
            sensor3 = random.randint(0, 100)
            self.current_reading = "sensor1:{},sensor2:{},sensor3:{}".format(sensor1, sensor2, sensor3)
            self.update_latest_value()
            time.sleep(delay)
    def update_latest_value(self):
        for sensor_chunk in self.current_reading.split(","):
            p = sensor_chunk.find(":") # point to split on
            sensor_name = sensor_chunk[0:p] # dictionary key
            self.current_values[sensor_name] = float(sensor_chunk[p+1:]) # set the correct value
    def get_current_values(self):
        return self.current_values
    def get_value(self, sensor_name):
        return self.current_values[sensor_name]
