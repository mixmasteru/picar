from picar.SunFounder_PCA9685.Servo import Servo
import time

if __name__ == '__main__':
    servo1 = Servo(0, bus_number=1, offset=0)
    servo1.write(90)
    time.sleep(1)
    servo1.write(0)
    time.sleep(1)

    servo2 = Servo(1, bus_number=1, offset=0)
    servo2.write(90)
    time.sleep(1)
    servo2.write(0)
    time.sleep(1)

    servo3 = Servo(2, bus_number=1, offset=0)
    servo3.write(90)
    time.sleep(1)
    servo3.write(0)
    time.sleep(1)
