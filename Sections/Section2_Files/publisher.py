#!/usr/bin/env python3

import rospy
from aa274a_s2.msg import MyMessage

def publisher():
    pub = rospy.Publisher('group05_topic', MyMessage, queue_size=10)
    rospy.init_node('my_node', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        message_to_pass = MyMessage()
        message_to_pass.str_data = 'hello world'
        message_to_pass.int_data = 2022
        message_to_pass.float_data = 10.1
        pub.publish(message_to_pass)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

