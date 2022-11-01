
#!/usr/bin/env python3

# Need to enable i2c slowdown on Raspberry Pi device tree overlay
# import board
# import busio
# import adafruit_bno055 as IMU


import logging
import sys
import time


from Adafruit_BNO055 import BNO055

class Imu:
    def __init__(self):
        self.bno = BNO055.BNO055(serial_port='/dev/serial0')
        if not self.bno.begin():
            raise RuntimeError('Failed to iniitialize BNO055! Is the sensor connected?')

        # Print system status and self test result.
        status, self_test, error = self.bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        # Print out an error if system status is in error mode.
        if status == 0x01:
            print('System error: {0}'.format(error))
            print('See datasheet section 4.3.59 for the meaning.')

        # Print BNO055 software revision and other diagnostic data.
        sw, bl, accel, mag, gyro = self.bno.get_revision()
        print('Software version:   {0}'.format(sw))
        print('Bootloader version: {0}'.format(bl))
        print('Accelerometer ID:   0x{0:02X}'.format(accel))
        print('Magnetometer ID:    0x{0:02X}'.format(mag))
        print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))


    def get_acceleration(self):
        """Return 3-tuple of X, Y, Z axis accelerometer values in m/s^2."""
        return self.bno.read_accelerometer()

    def get_euler_angles(self):
        """Returns 3-tuple of orientation Euler angle values."""
        yaw, roll, pitch = self.bno.read_euler()
        return yaw, roll, pitch

    def get_linear_acceleration(self):
        """Returns 3-tuple of X, Y, Z linear acceleration values (without effect of gravity) in m/s^2."""
        return self.bno.read_linear_acceleration()

