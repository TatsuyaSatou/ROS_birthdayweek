#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String 

def cb(message):
      rospy.loginfo(message.data)
def cb2(message):
      rospy.loginfo(message.data)
def cb3(message):
      rospy.loginfo(message.data)
def cb4(message):
      rospy.loginfo(message.data)
def cb5(message):
      rospy.loginfo(message.data)
if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    sub2 = rospy.Subscriber('count2_up', String, cb2) 
    sub3 = rospy.Subscriber('count3_up', String, cb3) 
    sub4 = rospy.Subscriber('count4_up', String, cb4) 
    sub5 = rospy.Subscriber('count5_up', String, cb5) 
    rospy.spin()
