#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("data is: %s", data.data)
    if data.data == "red":
        rospy.loginfo("yes: RED")
    elif data.data == "nred":
        rospy.loginfo("no: RED")
    elif data.data == "yellow":
        rospy.loginfo("yes: YELLOW")
    elif data.data == "nyellow":
        rospy.loginfo("no: YELLOW")
    elif data.data == "green":
        rospy.loginfo("yes: GREEN")
    elif data.data == "ngreen":
        rospy.loginfo("no: GREEN")
    else:
        rospy.loginfo("no: NOTHING", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
