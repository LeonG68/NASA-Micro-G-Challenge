import serial
import time

class Arduino:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flush()
        self.listeners = {}
        self.i = 0

    def send(self):
        """Sends a string to the Arduino"""
        
        while True:
            self.ser.write((str(self.i) + "\n").encode('utf-8'))
            line = self.ser.readline().decode('utf-8').rstrip()
            print(line)
            self.i += 1
            time.sleep(1)
