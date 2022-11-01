from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

def initialize():
    arduino = Arduino()
    thrusters = SpeedController(arduino)
    drive = Drive(thrusters)
    #imu = Imu()
    radio = KerberosSDR()
    for i in range(8):
        drive.tank_drive(0, 0, 0)

    return drive, radio, arduino

def main():
    models = initialize()

    robot = Robot(*models)
    
    #delay
    #time.sleep(2)

    while True:
        robot.simple_drive(SCALE)
        time.sleep(1 / CYCLES_PER_SECOND)
        #time.sleep(3)

if __name__ == "__main__":
    main()
