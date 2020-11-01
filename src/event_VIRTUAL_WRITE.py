#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
import BlynkLib

BLYNK_AUTH = 'gASisGlaGebx-uTQn6zKU0H1Fw45v4aj'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler
@blynk.on("V3")
#def v3_write_handler(value):
#    print('Current slider value: {}'.format(value[0]))
def v3_slicer(value):
    x = value[0]
    print(x)

@blynk.on("V4")
def v4_button(value):
    print ("Han pulsado el boton")
    print(value[0])
    x = value[0]
    if x == "0":
        print ("El valor es 0")
        aux = False
    else:
        aux = True
        print ("El valor es 1")
    pub.publish(aux)

if __name__ == '__main__':
    rospy.init_node('blynk_printer', anonymous=True)
    pub = rospy.Publisher('switch_printer', Bool, queue_size=10)
    while True:
        blynk.run()
