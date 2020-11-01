#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int16MultiArray
import BlynkLib

BLYNK_AUTH = 'gASisGlaGebx-uTQn6zKU0H1Fw45v4aj'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

rgb = Int16MultiArray()
rgb.data=[0,0,0]

#Button for printer is pressed
@blynk.on("V3")
def v4_button(value):
    print("ON: " + value[0])
    x = value[0]
    if x == "0":
        aux = False
    else:
        aux = True
    print_pub.publish(aux)


@blynk.on("V4")
def v4_button(value):
    print("RED: " + value[0])
    rgb.data[0] = value[0]
    leds_pub.publish(rgb)

@blynk.on("V5")
def v4_button(value):
    print("GREEN: " + value[0])
    rgb.data[1] = value[0]
    leds_pub.publish(rgb)

@blynk.on("V6")
def v4_button(value):
    print("RED: " + value[0])
    rgb.data[2] = value[0]
    leds_pub.publish(rgb)

if __name__ == '__main__':
    rospy.init_node('blynk_printer', anonymous=True)
    print_pub = rospy.Publisher('switch_printer', Bool, queue_size=10)
    leds_pub = rospy.Publisher('switch_rgb', Int16MultiArray, queue_size=10)

    while True:
        blynk.run()
