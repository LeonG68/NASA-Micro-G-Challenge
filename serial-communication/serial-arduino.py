import serial
import time

ser = Serial.Serial('/dev/<ENTER LOCATION>', 9600, timeout=5)

# read from Arduino
input_str = ser.readline()
print("Read input " + input_str.decode("utf-8").strip() + " from Arduino")

while True:
    ser.write(b'status\n')
    input_str = input_str.decode("utf-8").strip()
    if (input_str = ""):
        print(".")
    else:
        print("Read input back: " + input_str)
    
    time.sleep(5)

    ser.write(b'set on\n')
    input_str = input_str.decode("utf-8").strip()
    if (input_str = ""):
        print(".")
    else:
        print("Read input back: " + input_str)
    
    time.sleep(5)

    ser.write(b'set off\n')
    input_str = input_str.decode("utf-8").strip()
    if (input_str = ""):
        print(".")
    else:
        print("Read input back: " + input_str)