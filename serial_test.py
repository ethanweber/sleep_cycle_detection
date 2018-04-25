import serial
import time
ser = serial.Serial('/dev/cu.usbmodem14611', 115200)
while True:
    line = ser.readline().decode()
    # angle = float(line[0:line.find('\r')]) # grab the number
    # print(angle)
    print(line)
    time.sleep(0.01)
