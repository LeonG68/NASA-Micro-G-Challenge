  
from .arduino import Arduino
#from .imu import Imu
from .kerberos_sdr import KerberosSDR

class SpeedController:

    def __init__(self, arduino: Arduino):
        self.arduino = arduino
        #self.thisImu = Imu()
        self.kerberos = KerberosSDR()
        # set dt to loop time.
        # D means derivative. xD means velocity. xDD means acceleration.

        self.dt = 0.05
        self.t = 0
        self.currentAngle = 0
        self.originalAngle = 0
        self.totalAngleError = 0

        self.MAX_FORWARD = 2.71
        self.MAX_BACKWARDS = 2.90

        self.MAX_SPEED_FORWARD = 1 #???
        self.MAX_SPEED_BACKWARDS = 1 #??



    #calling thrusttoPwm: pass in level * forward/backward
    def set_speed(self, speed1: float, speed2: float, scale):
        """Runs the thruster at a specified speed between 1 (full speed forward) and -1 (full speed backward)"""
        # thrust1, thrust2 = 0, 0
        # if speed1 > 0:
        #     velocity1 = speed1 * self.MAX_SPEED_FORWARD
        # else:
        #     velocity1 = speed1 * self.MAX_SPEED_BACKWARDS
        # if speed1 > 0:
        #     velocity2 = speed2 * self.MAX_SPEED_FORWARD
        # else:
        #     velocity2 = speed2 * scale *self.MAX_SPEED_BACKWARDS
        # thrust1 = self.getPWM(velocity1, scale)
        # thrust2 = self.getPWM(velocity2, scale)
        # self.arduino.send("{0}{1}{2}".format(round(self.thrustToPWM(thrust1)), "|", round(self.thrustToPWM(thrust2))))

        self.arduino.send("{0}{1}{2}".format(round(self.getPWM(speed1, scale)), "|", round(self.getPWM(speed2, scale))))

    def set_speed2(self, desiredVelocity: float):
        
        thrust1 = self.getThrust(desiredVelocity)
        thrust2 = self.getThrust(desiredVelocity)
        self.arduino.send("{0}{1}{2}".format(round(self.thrustToPWM(thrust1)), "|", round(self.thrustToPWM(thrust2))))

    def set_speed_imu_orientation(self, desiredVelocity: float):
        
        thrust = []
        thrust = self.getThrust(desiredVelocity)
        #thrust2 = self.getThrust(desiredVelocity)
        print(thrust)
        self.arduino.send("{0}{1}{2}".format(round(self.thrustToPWM(thrust[0])), "|", round(self.thrustToPWM(thrust[1]))))
    
    #Tracks orientation and implements PID control to straighten vehicle
    #write getThrust(self,desiredVelocity,desiredAngle) for kerbrose, set original angle to desired angle every time.
    

    ########### LEON GUO CODE ############
    # def getThrust(self, desiredVelocity):

    #     #loop this every dt seconds
    #     #find out which euler angle we need


    #     self.t = self.t + self.dt
        
    #     doa_angle = self.kerberos.getDOA()
    #     print("Kerbrose Angle: ", doa_angle)

    #     # when time is less than .5 seconds, make sure drone is steady to correct for sensor biases.

    #     if doa_angle <= 180:
    #     	self.currentAngle = doa_angle
    #     else:
    #     	self.currentAngle = -1*(360- doa_angle)

    #     self.totalAngleError = self.totalAngleError + (self.currentAngle)
        
    #     #From Meeting: Testing today, print out the angle, see how angle output reacts when offset to the left and right. Change the if statement correspondingly. 
    #     #Figure out which motor is thrust one/two. Left or right?
    #     #New logic, if using 360, if greater than 180 turn one direction, less than turn another.
    #     #Match up the thrust with the motors
        
    #     #Tune the values of the controllers. First put the drone in the water. Set the desired velocity to a very low value. Leave the drone for two seconds. Once the drone starts running, you give #the drone an offset error.
        
    #     #Switch depending on thruster orientation
    #     #New logic, if using 360, if greater than 180 turn one direction, less than turn another.
    #     outputThrust = []
    #     if (self.currentAngle < self.originalAngle):
            
    #         # outputThrust.append(desiredVelocity)
    #         # outputThrust.append((0*(desiredVelocity) * (self.originalAngle - self.currentAngle)) + (0 * (desiredVelocity) * self.totalAngleError/50))
            
    #         outputThrust = [desiredVelocity, (0*(desiredVelocity) * (0 - self.currentAngle)) + (0 * (desiredVelocity) * self.totalAngleError/50)]
    #         return outputThrust
    #     else:
    #         # outputThrust.append(0*(desiredVelocity) * (self.originalAngle - self.currentAngle) + 0 * (desiredVelocity) * self.totalAngleError/50)
    #         # outputThrust.append(desiredVelocity)
    #         outputThrust = [0*(desiredVelocity) * (0 - self.currentAngle) + 0 * (desiredVelocity) * self.totalAngleError/50, desiredVelocity]
    #         return outputThrust
            

    # def thrustToPWM(self, thrust):
    #     PWM = 0
    #     if thrust > 0:
    #         PWM = -32.289500442873752 * thrust ** 2 + 3.869011829925794 * thrust ** 3 + 162.816482640325944 * thrust + 1537.793648693580053
    #     else:
    #         if thrust <= 0: #should this be < rather than <=??
    #             PWM = 47.581695898375777 * thrust ** 2 + -7.292251741725251 * thrust ** 3 + -199.610465634680764 * thrust + 1460.832024027741454

    #     if PWM < 1820 and PWM > 1100:
    #         print(PWM)
    #         return PWM
    #     else:
    #         print(PWM)
    #         if PWM > 3000 or PWM < 0:
    #             return 1500
    #         elif PWM > 1820:
    #             return 1820
    #         else:
    #             return 1100


###### TEST CODE #####
    def getPWM(self, level, scale): # level is between -1 to 1 where < 0 means backwards and > 0 means forward.
        # Gets the PWM
        
        level *= scale

        if level < -1 or level > 1:
            return "Incorrect input"

        if level == 0:
            return 1500.00
        elif level > 0:
            return self.thrustToPWM(level * self.MAX_FORWARD) 
        elif level < 0:
            return self.thrustToPWM(level * self.MAX_BACKWARDS)
        
    def thrustToPWM(self, thrust):
        # fitted a polynomial to make it easy to map thrust to pwm
        if thrust > 0:
            return -32.289500442873752 * thrust ** 2 + 3.869011829925794 * thrust ** 3 + 162.816482640325944 * thrust + 1537.793648693580053
        else:
            thrust *= -1
            return 47.581695898375777 * thrust ** 2 + -7.292251741725251 * thrust ** 3 + -199.610465634680764 * thrust + 1460.832024027741454
