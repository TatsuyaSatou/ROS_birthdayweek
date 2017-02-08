#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import datetime
import sys

args = sys.argv[1:]

 
tosi = int(args[0]) 
n = 0
if __name__ == '__main__': 
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    pub2 = rospy.Publisher('count2_up',String, queue_size=50)
    pub3 = rospy.Publisher('count3_up',String, queue_size=50)
    pub4 = rospy.Publisher('count4_up',String, queue_size=50)
    pub5 = rospy.Publisher('count5_up',String, queue_size=50)
    rate = rospy.Rate(0.3)
    while not rospy.is_shutdown():
       while n <= 100: 
	    birthday = datetime.date(tosi,int(args[1]),int(args[2]))
            week = {0: '月曜日' ,1: '火曜日' ,2: '水曜日' ,3: '木曜日' ,4: '金曜日' ,5: '土曜日' ,6: '日曜日'}
            weekdays =  week[birthday.weekday()]
            pub.publish(n)
            pub2.publish(weekdays)
            if birthday.weekday() < 4:
                  pub3.publish('平日だけど頑張ろう！！')
            elif birthday.weekday() == 4:
                  pub4.publish('花金だ！！仕事はちゃっちゃと片付けて呑みに行こう！！')
            else:
                  pub5.publish('最高の誕生日！のはず。休みだから遊びほうけよう！！')
            tosi +=  1
            n += 1
            rate.sleep()
