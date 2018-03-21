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
    def connect(self):
        serial_port = serial.Serial(port, baud, timeout=0)
        self.connect = True
    # this will start the thread that runs in the background
    def start(self):
        self.thread.start()
    def while_reading_loop(self):
        while self.connected:
            self.current_reading = self.serial_port.readline().decode()
    def get_latest_value(self):
        return self.current_reading
