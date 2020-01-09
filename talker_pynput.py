#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pynput import keyboard

#def on_press(key):
#    print("press key is: " + key.char)
#    rospy.loginfo("press key is: " + key.char)
#    pub.publish("pressed")
    
#def on_release(key):
#    print("release key is: " + key.char)
#    rospy.loginfo("release key is: " + key.char)
#    pub.publish("released")

def talker():
    def on_press(key):
        rospy.loginfo("press key is: " + key.char)
        #pub.publish("pressed: " + key.char)
        if key.char == 'a':
            pub.publish('red')
        elif key.char == 's':
            pub.publish('yellow')
        elif key.char == 'd':
            pub.publish('green')        

    def on_release(key):
        rospy.loginfo("release key is: " + key.char)
        #pub.publish("released: " + key.char)
        if key.char == 'a':
            pub.publish('no-red')
        elif key.char == 's':
            pub.publish('no-yellow')
        elif key.char == 'd':
            pub.publish('no-green')

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('driver', anonymous=True)
    rate = rospy.Rate(10)
    
    # begin scankey program
    rospy.loginfo('Control LED by ASD key.')
    pub.publish("start")

    # non-blocking
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    #rospy.spin()
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    talker()
