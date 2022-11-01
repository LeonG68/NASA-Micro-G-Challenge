from constants import *
from typing import Callable
import serial, time 

class Arduino:
    def __init__(self):
        self.ser = serial.Serial(ARDUINO_PORT, ARDUINO_BAUDRATE, timeout=SERIAL_TIMEOUT)
        self.ser.flush()
        self.listeners = {}

    def update(self):
        """call this in the robot loop to receive signals"""
        
        line = self.ser.readline()
        if line:
            line = line.decode('utf-8').rstrip()
            for callback, condition in self.listeners.items():
                if condition(line):
                    callback(line)

    def send(self, msg: str):
        """Sends a string to the Arduino"""
        self.ser.write((msg + "\n").encode('utf-8'))
        time.sleep(1 / CYCLES_PER_SECOND)
        print("MSG: ", msg)
        print("Decode: " , self.ser.readline().decode('utf-8'), "\n\n")
        

    def subscribe(self, callback: Callable[[str], None], condition: Callable[[str], bool] = lambda x: True):
        """Subscribe to messages from the Arduino. Optionally provide a condition in order to call the callback."""
        self.listeners[callback] = condition

    def unsubscribe(self, callback: Callable[[str], None]):
        """Unsubscribe from messages to the Arduino."""
        if callback in self.listeners:
            del self.listeners[callback]
