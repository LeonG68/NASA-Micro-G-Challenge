import time
from datetime import datetime
from models import Imu


def test_imu():
    """Tests all sensors of IMU."""
    while True:
        print(datetime.now().time())
        print("Accelerometer (m/s^2): {}".format(imu.get_acceleration()))
        print("Gyroscope (rad/sec): {}".format(imu.get_gyro()))
        print("Euler angle: {}".format(imu.get_euler_angles()))
        print("Quaternion: {}".format(imu.get_quaternion()))
        print("Linear acceleration (m/s^2): {}".format(imu.get_linear_acceleration()))
        print("Gravity (m/s^2): {}".format(imu.get_gravity()))
        time.sleep(1)


def test_accelerometer():
    while True:
        print(datetime.now().time())
        print("Accelerometer (m/s^2): {}".format(imu.get_acceleration()))
        time.sleep(1)


def test_gyroscope():
    while True:
        print(datetime.now().time())
        print("Gyroscope (rad/sec): {}".format(imu.get_gyro()))
        time.sleep(1)


def test_euler_angles():
    while True:
        print(datetime.now().time())
        print("Euler angle: {}".format(imu.get_euler_angles()))
        time.sleep(1)


def test_quaternion():
    while True:
        print(datetime.now().time())
        print("Quaternion: {}".format(imu.get_quaternion()))
        time.sleep(1)


def test_linear_acceleration():
    while True:
        print(datetime.now().time())
        print("Linear acceleration (m/s^2): {}".format(imu.get_linear_acceleration()))
        time.sleep(1)


def test_gravity():
    while True:
        print(datetime.now().time())
        print("Gravity (m/s^2): {}".format(imu.get_gravity()))
        time.sleep(1)


if __name__ == "__main__":
    # Choose which tests you want to run by commenting/uncommenting
    imu = Imu()
    test_imu()
    # test_accelerometer()
    # test_gyroscope()
    # test_euler_angles()
    # test_quaternion()
    # test_linear_acceleration()
    # test_gravity()