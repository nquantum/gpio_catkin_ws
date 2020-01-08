#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pynput import keyboard

i = ""

def on_press(key):
    try:
        print(key.char)
        i = key.char
    except AttributeError:
        pass
    #if key.char == 'a':
    #    rospy.loginfo('RED')
    #    pub.publish('red')
    #elif key.char == 's':
    #    rospy.loginfo('YELLOW')
    #    pub.publish('yellow')
    #elif key.char == 'd':
    #    rospy.loginfo('GREEN')
    #    pub.publish('green')
    #else: def on_release(key):
    #print('{0} released'.format(
    #    key))
    #if key == keyboard.Key.esc:
    # Stop listener
    #    return False
    #    rospy.loginfo('none')
    #time.sleep(1)

def on_release(key):
    #if key == keyboard.Key.esc:
    # Stop listener
    #    return False
    try:
        print(key.char)
        i = key.char
    except AttributeError:
        pass

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('driver', anonymous=True)
    rate = rospy.Rate(10)

    rospy.loginfo('Control LED by ASD key.')

#    with keyboard.Listener(
#            on_press=on_press,
#            on_release=on_release) as listener:
#        listener.join()

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    while not rospy.is_shutdown():
        rospy.loginfo(i)
        pub.publish(i)
        rate.sleep()

if __name__ == '__main__':
    talker()
