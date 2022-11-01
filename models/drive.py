from .speed_controller import SpeedController

class Drive:
    def __init__(self, thrusters: SpeedController):
        self.thrusters = thrusters

    def tank_drive(self, left: float, right: float, scale):
        self.thrusters.set_speed(left, right, scale)

    def arcade_drive(self, forward: float, turn: float, scale):
        """
        Control robot by forward speed and turn speed, both -1 to 1. 
        Positive turn for clockwise, negative for counterclockwise
        """
        left = forward + turn
        right = forward - turn

        # normalize values to 1 if too big
        scale_factor = max(1, abs(left), abs(right))
        left /= scale_factor
        right /= scale_factor

        self.tank_drive(left, right, scale)

    def tank_drive2(self, desiredVelocity: float):
        self.thrusters.set_speed2(desiredVelocity)

    def tank_drive_imu_orientation(self, desiredVelocity: float):
        self.thrusters.set_speed_imu_orientation(desiredVelocity)