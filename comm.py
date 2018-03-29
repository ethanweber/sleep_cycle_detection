# this code is to interface w/ our microcontroller via serial over USB

# serial library to talk with microcontroller
import serial
import io
import threading

class USBCommunication:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.connected = False
        self.serial_port = None
        self.current_reading = None
        self.thread = threading.Thread(target=while_reading_loop, args=(serial_port,))
        # current_values is a dictionary for the sensors and their current readings
        self.current_values = {}å
    def connect(self):
        serial_port = serial.Serial(port, baud, timeout=0)
        self.connect = True
    # this will start the thread that runs in the background
    def start(self):
        self.thread.start()
    def while_reading_loop(self):
        while self.connected:
            self.current_reading = self.serial_port.readline().decode()
            self.update_latest_value()
    def update_latest_value(self):
        for sensor_chunk in self.current_values.split(","):
            sensor_name = sensor_chunk[0:sensor_chunk.find(":")]
            self.current_values[key] = value
    def get_current_values(self):
        return self.current_values
