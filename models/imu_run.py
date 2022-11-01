from imu import Imu
import time

myImu = Imu()

while 1:
    print(myImu.get_acceleration())
    time.sleep(1)