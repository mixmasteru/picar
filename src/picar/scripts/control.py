#!/usr/bin/python3

import sys

import rospy
from geometry_msgs.msg import Twist
from picar.backwheels import BackWheels
from picar.frontwheels import FrontWheels
from picar.setup_car import Setup


class Control:

    def __init__(self):
        # Setup.setup()
        forward_speed = 50
        backward_speed = 50
        rospy.Subscriber("cmd_vel", Twist, self.callback)
        self.bw = BackWheels()
        self.fw = FrontWheels()

    def callback(self, msg):
        rospy.loginfo(rospy.get_caller_id() + "Twist %s", msg)

        if msg.linear.x > 0.1:
            self.bw.forward()
            self.bw.speed = int(100 * msg.linear.x)
        elif msg.linear.x < -0.1:
            self.bw.backward()
            self.bw.speed = int(100 * -msg.linear.x)
        else:
            self.bw.stop()

        if msg.angular.z > 0.1 or msg.angular.z < -0.1:
            self.fw.turn(int(90 - 40 * msg.angular.z))
        else:
            self.fw.turn_straight()

    def stop(self):
        rospy.loginfo("STOP")
        self.bw.stop()
        self.fw.turn_straight()

# if __name__ == '__main__':
#    main(sys.argv)
