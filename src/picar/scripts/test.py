import time
from picar import back_wheels
from picar import front_wheels
from picar.setup_car import Setup
from picar.PCF8591 import test
import picar

if __name__ == '__main__':
    setup = Setup()
    bw = back_wheels.BackWheels(db='config')
    fw = front_wheels.FrontWheels(db='config')
    bw.forward()
    bw.speed = 100
    time.sleep(2)
    bw.stop()
    bw.backward()
    bw.speed = 100
    time.sleep(2)
    bw.stop()

    fw.calibration()
    fw.turn_left()
    time.sleep(1)
    fw.turn_right()
    time.sleep(1)
    fw.turn_straight()
