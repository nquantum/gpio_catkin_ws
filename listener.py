#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo("in call back")
    #rospy.loginfo("data is: %s", data.data)
    if data.data == "red":
        rospy.loginfo("yes: RED")
    elif data.data == "no-red":
        rospy.loginfo("no: RED")
    elif data.data == "yellow":
        rospy.loginfo("yes: YELLOW")
    elif data.data == "no-yellow":
        rospy.loginfo("no: YELLOW")
    elif data.data == "green":
        rospy.loginfo("yes: GREEN")
    elif data.data == "no-green":
        rospy.loginfo("no: GREEN")
    else:
        rospy.loginfo("nothing: NOT MATCH")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.loginfo("start listen through /chatter")
    rospy.spin()

if __name__ == '__main__':
    listener()
