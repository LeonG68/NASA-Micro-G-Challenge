from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

TEST_SCALE = 0.1
DURATION = 3
TURNTIME = 2
INCREMENTS = 2
LAST = 10
MAXPWM = 4

class ManualTestAcceleration:
        def __init__(self):
            self.arduino = Arduino()
            self.thrusters = SpeedController(self.arduino)
            self.drive = Drive(self.thrusters)
            #imu = Imu()
            self.radio = KerberosSDR()

            self.robot = Robot(self.drive, self.radio, self.arduino)

            for i in range(8):
                self.drive.tank_drive(0, 0, TEST_SCALE)


        def accelerate_test(self, duration=DURATION, increments=INCREMENTS):
            print("Acceleration")
            # start with scale of 0.1, increment by 0.3 for each iteration
            self.drive.tank_drive(0, 0, duration)
            time.sleep(3)
            last = 0
            for i in range(1, 10, increments):
                last = i
                x = i / 10
                # keeps current speed for duration
                self.drive.tank_drive(1, 1, x)
                time.sleep(duration)

            #uncomment when not running manualtest

            #self.drive.tank_drive(0, 0, 0)
            #time.sleep(3)
            return last


        def decelerate_test(self, duration=DURATION, last=LAST, increments=INCREMENTS):
            print("Deceleration")
            # start with scale of 1, decrement by 0.3 for each iteration

            #uncomment when not using manualtest

            #self.drive.tank_drive(0, 0, duration)
            #time.sleep(3)

            
            for i in range(0, 10, increments):
                x = (last - i) / 10
                if x < .1:
                    x = .1
                self.drive.tank_drive(1, 1, x)
                # keeps current speed for duration
                time.sleep(duration)
            self.drive.tank_drive(0, 0, 0)
            time.sleep(3)

        def stop(self):
            for i in range(8):
                self.drive.tank_drive(0, 0, 0)

        def naturaldeceleration(self, maxPWM=MAXPWM):
            self.drive.tank_drive(0, 0, 0)
            time.sleep(3)
            for i in range(1, maxPWM):
                x = i / 10
                self.drive.tank_drive(1, 1, x)
                time.sleep(1)
            time.sleep(6)
            self.drive.tank_drive(0, 0, 0)

        def scalereverse(self, maxPWM=MAXPWM):
	    self.drive.tank_drive(0, 0, 0)
	    time.sleep(3)
	    x = maxPWM / 10
	    self.drive.tank_drive(1, 1, x)
	    time.sleep(5)
	    self.drive.tank_drive(1, 1, -x)
	    time.sleep(5)
	    self.drive.tank_drive(0, 0, 0)

            
        def manualtest(self, duration=DURATION, increments=INCREMENTS):
            
            # test acceleration and deceleration
            last = self.accelerate_test(duration, increments)
            time.sleep(1)
            self.decelerate_test(duration, last, increments)

