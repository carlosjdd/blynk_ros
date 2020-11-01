#!/usr/bin/python

# import the necessary packages
import rospy
import BlynkLib

# import the necessary msgs. Example with msg type String_Int_Arrays:
from std_msgs.msg import Bool

BLYNK_AUTH = 'gASisGlaGebx-uTQn6zKU0H1Fw45v4aj'

        # Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

class printer():
    """ Class class_name.

    Info about the class
    """

    def __init__(self):
        """Class constructor

        It is the constructor of the class. It does:
        """

        #Subscribe to ROS topics
        self.printer_pub = rospy.Publisher('switch_printer', Bool, queue_size=10)

        print("[INFO] Node started")


    def run_loop(self):
        """ Infinite loop.

        When ROS is closed, it exits.
        """
        while not rospy.is_shutdown():
            #functions to repeat until the node is closed
            blynk.run()

    def stopping_node(self):
        """ROS closing node

        Is the function called when ROS node is closed."""
        print("\n\nBye bye! :)\n\n")

    # Register virtual pin handler
    @blynk.on("V3")
    def v3_slicer(self, value):
        x = value[0]
        print(x)

    @blynk.on("V4")
    def v4_button(self, value):
        print ("Han pulsado el boton")
        print(value[0])
        x = value[0]
        if x == "0":
            print ("El valor es 0")
            aux = False
        else:
            aux = True
            print ("El valor es 1")

        self.printer_pub.publish(aux)


if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - Start the node
    - Create an object of the class
    - Run the node

    """
    try:
        rospy.init_node('blink_printer')       # Init ROS node

        blynk_printer = printer()
        rospy.on_shutdown(blynk_printer.stopping_node)   #When ROS is closed, this void is executed

        blynk_printer.run_loop()

    except rospy.ROSInterruptException:
        pass
