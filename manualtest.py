from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

DESIRED_VELOCITY = 0.5
TEST_SCALE = 0.5
DURATION = 1
TURNTIME = 5
REVERSE_SCALE = 1


class ManualTest:
    def __init__(self):
        self.arduino = Arduino()
        self.thrusters = SpeedController(self.arduino)
        self.drive = Drive(self.thrusters)
        #self.imu = Imu()
        self.radio = KerberosSDR()
    

        self.robot = Robot(self.drive, self.radio, self.arduino)

        for i in range(8):
            #self.drive.tank_drive(0, 0, TEST_SCALE)
            self.drive.tank_drive_imu_orientation(0.0)

####### STOPPING BOAT #######
    def stop(self):
        for i in range(8):
            self.drive.tank_drive(0, 0, 0)

############################################
############## LINEAR TESTS ################
############################################

    def reverse(self, duration=DURATION, scale=REVERSE_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        #val = int(scale*10)
        for i in range(scale+1):
            x = i / 10
            self.drive.tank_drive(-1,-.91,x)
            time.sleep(duration)

    def straight_test(self):
        # turntime = 2 #tested value for how long it takes to turn 180
        # go straight and back test
        for x in range(1, 5):
            self.straight_test_params(DURATION, TEST_SCALE)
            self.turn_right_test(TURNTIME, TEST_SCALE)
            self.straight_test_params(DURATION, TEST_SCALE)
            self.turn_right_test(TURNTIME, TEST_SCALE)

    def straight_speed(self):
        # go straight and back test, straight speed
        for x in range(10):
            scale = (x+1)/10
            self.straight_test_params(DURATION, scale)
            self.turn_right_test(TURNTIME, TEST_SCALE)
            self.straight_test_params(DURATION, scale)
            self.turn_right_test(TURNTIME, TEST_SCALE)

    def straight_test_params(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        val = int(scale*10)
        for i in range(val):
            x = i / 10
            self.drive.tank_drive(.8,1,x)
            time.sleep(duration)

    def straight_right(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale)
        #time.sleep(duration)
        self.drive.tank_drive(1, 0.8, scale)

    def straight_left(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale)
        #time.sleep(duration)
        self.drive.tank_drive(0.7, 1, scale)

    def straight_left_right(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale)
        #time.sleep(duration)
        self.drive.tank_drive(0.2, 1, scale)
        time.sleep(duration)
        self.drive.tank_drive(1, 0.6, scale)
        time.sleep(duration+1)
        self.drive.tank_drive(0.7, 1, scale)


    def straight_reverse(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0,0,scale)
        time.sleep(duration)
        self.straight_test_params(duration, scale)
        self.drive.tank_drive(0,0,0)
        time.sleep(.1)
        self.drive.tank_drive(-.5, -1, .5)

############################################
############### TURN TESTS #################
############################################

    def turn_right_test(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        self.drive.tank_drive(0.5, 0, scale)
        #self.drive.tank_drive(1, 0.2473, scale)
        #self.drive.tank_drive(1, 0.6, scale)
        #self.drive.tank_drive(1, 0.8124, scale)
        #self.drive.tank_drive(1, 0.9156, scale)
        #self.drive.tank_drive(1, 0.9572, scale)

        time.sleep(duration)
        self.drive.tank_drive(0, 0, scale)
        time.sleep(3)

    def turn_left_test(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        self.drive.tank_drive(0, 0.5, scale)
        #self.drive.tank_drive(0.2473, 1, scale)
        #self.drive.tank_drive(0.6, 1, scale)
        #self.drive.tank_drive(0.8124, 1, scale)
        #self.drive.tank_drive(0.9156, 1, scale)
        #self.drive.tank_drive(0.9572, 1, scale)
        time.sleep(duration)
        self.drive.tank_drive(0, 0, scale)
        time.sleep(3)


    def turn_test(self):
        #turn_right_test() and turn_left_test()
        for y in range(10):
            scale = (y+1)/10
            for x in range(1, 5):
                self.turn_right_test(x, scale)
                self.turn_left_test(x, scale)

    def hard_turn_right(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        val = int(scale*10)
        for i in range(val):
            x = i / 10
            self.drive.tank_drive(1,-1,x)
            time.sleep(duration)


    def hard_turn_left(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        val = int(scale*10)
        for i in range(val):
            x = i / 10
            self.drive.tank_drive(-1,1,x)
            time.sleep(duration)


    def ast(self, desiredVelocity=DESIRED_VELOCITY, scale=SCALE, duration=DURATION):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        for _ in range(500):
            self.drive.tank_drive2(desiredVelocity)
            time.sleep(.05)

        self.drive.tank_drive(0, 0, 0)

    

    def skrt(self, duration=DURATION, scale=TEST_SCALE, turntime=TURNTIME):
        self.drive.tank_drive(0,0,0)
        time.sleep(2)
        self.straight_test_params(duration, scale)
        self.drive.tank_drive(-.25,1,scale)
        time.sleep(turntime)
        self.drive.tank_drive(1,1,scale)

############################################
############## OTHER TESTS #################
############################################

    def return_time(self):
        return time.time()

    def dead_spin_test(self,
                       direction="left",
                       duration=10,
                       iteration=1,
                       speed=0,
                       func=None,
                       func_interval=0.2):
        STOP_DURATION = 5

        self.drive.tank_drive(0, 0, TEST_SCALE)
        time.sleep(STOP_DURATION)

        for i in range(iteration):
            self.drive.tank_drive(0.5, 0, TEST_SCALE)
            for t in range(duration / func_interval):
                func()
                time.sleep(func_interval)
            self.drive.tank_drive(0, 0, TEST_SCALE)
            time.sleep(STOP_DURATION)

    def euler_angle_test(self, iteration=1, func_interval=0.2):
        dead_spin_test(iteration=iteration, func_interval=func_interval)

    def dump_euler_angles(self):
        imu = Imu()
        EULER_SPIN_LOG.add(str(imu.get_euler_angles()))

    def thruster_test(self):
        self.drive.tank_drive(0,0,0)
        time.sleep(2)
        self.drive.tank_drive(0, 1, .2)
        time.sleep(2)
        self.drive.tank_drive(0,0,0)

    def imu_angle_test(self, desiredVelocity=DESIRED_VELOCITY, scale=SCALE, duration=DURATION):
        self.drive.tank_drive_imu_orientation(0)
        time.sleep(duration)
        for _ in range(500):
            self.drive.tank_drive_imu_orientation(desiredVelocity)
            time.sleep(.25)

        self.drive.tank_drive_imu_orientation(0)

