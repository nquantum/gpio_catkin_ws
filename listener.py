#!/usr/bin/env python
import rospy
from std_msgs.msg   import String
from gpiozero       import LED

red     = LED(2)
yellow  = LED(3)
green   = LED(4)

def callback(data):
    #rospy.loginfo("in call back")
    #rospy.loginfo("data is: %s", data.data)
    if data.data == "red":
        rospy.loginfo("yes: RED")
        red.on()
    elif data.data == "no-red":
        rospy.loginfo("no: RED")
        red.off()
    elif data.data == "yellow":
        rospy.loginfo("yes: YELLOW")
        yellow.on()
    elif data.data == "no-yellow":
        rospy.loginfo("no: YELLOW")
        yellow.off()
    elif data.data == "green":
        rospy.loginfo("yes: GREEN")
        green.on()
    elif data.data == "no-green":
        rospy.loginfo("no: GREEN")
        green.off()
    else:
        rospy.loginfo("nothing: NOT MATCH")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.loginfo("start listen through /chatter")
    rospy.spin()

if __name__ == '__main__':
    listener()
