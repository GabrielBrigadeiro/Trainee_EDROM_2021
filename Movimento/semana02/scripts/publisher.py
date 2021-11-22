#!/usr/bin/env python3
# license removed for brevity
import rospy
from semana02.msg import atv2

def talker():
    pub = rospy.Publisher('publisher_pers', atv2, queue_size=10)
    rospy.init_node('talker_pers', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = atv2()
    msg.id = 21
    msg.position = 45.8
    msg.torque = True

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass