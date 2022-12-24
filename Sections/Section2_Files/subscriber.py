#!/usr/bin/env python3

import rospy
from aa274a_s2.msg import MyMessage

def callback(msg: MyMessage):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s, %d, %f", msg.str_data, msg.int_data, msg.float_data)

def subscriber():
    rospy.init_node('my_node', anonymous=True)
    rospy.Subscriber("group05_topic", MyMessage, callback)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
