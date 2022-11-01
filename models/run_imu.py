import . from imu

thisImu = Imu()

dt = 0.1
t = 0

#loop this (MainLoop)

acelVector = get_acceleration(self)
t = t + dt

if t < 2:
    x = 0
    y = 0
    z = 0
    xD = 0
    yD = 0
    zD = 0
    xDD = 0
    yDD = 0
    zDD = 0
    xDDCorr = acelVector[0]
    yDDCorr = acelVector[1]
    zDDCorr = acelVector[2]
else:
    xDD = acelVector[0] - xDDCorr
    yDD = acelVector[1] - yDDCorr
    zDD = acelVector[2] - zDDCorr

    xD = xD + xDD * dt
    yD = yD + yDD * dt
    zD = zD + zDD * dt

    desiredXVelocity = fill this in.

    velocityError = desiredVelocity - currentVelocity
    lastVelocityError = totalVelocityError
    totalVelocityError = totalVelocityError + velocityError * dt
    slopeVelocityError = (lastVelocityError - velocityError)/dt

    x = x + xD * dt
    y = y + yD * dt
    z = z + zD * dt

    outputPWM = 1000 * (desiredVelocity - currentVelocity) + 200 * totalVelocityError + 300 * slopeVelocityError

f = open("trackfile.txt", 'a')
f.write("Time: " + dt + " Acceleration " + xDD + ' ' + yDD + " " + zDD + ' Velocity' + xD + ' ' + yD + ' ' + zD)
f.close()
