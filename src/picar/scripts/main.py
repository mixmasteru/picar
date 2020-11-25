#!/usr/bin/python3

import rospy
import control
from picar.setup import Setup

if __name__ == '__main__':
    print("hello")
    setup = Setup()
    control = control.Control()

    rospy.init_node('control', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    except rospy.ROSInterruptException:
        control.stop()
        pass
    finally:
        control.stop()
