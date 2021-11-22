#!/usr/bin/env python3
import rospy
from semana02.msg import atv2

def callback(data):
    rospy.loginfo(rospy.loginfo("O ID, a posicao e o toque são %d, %f, %s" % (data.id, data.position, data.torque)))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener_pers', anonymous=True)

    rospy.Subscriber("publisher_pers", atv2, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()