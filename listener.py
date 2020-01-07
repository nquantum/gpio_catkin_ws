#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("data is: %s", data.data)
    if data.data == 'red':
        rospy.loginfo("yes: RED")
        rate = rospy.Rate(1)
        rate.sleep()
    elif data.data == 'yellow':
        rospy.loginfo("yes: YELLOW")
    elif data.data == 'green':
        rospy.loginfo("yes: GREEN")
    else:
        rospy.loginfo("no: %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("input", String, callback)
    #rate = rospy.Rate(10)
    rospy.spin()

if __name__ == '__main__':
    listener()
