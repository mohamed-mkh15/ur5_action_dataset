#!/usr/bin/env python

import rospy
from recorder import Recorder

if __name__ == '__main__':
    # Bag name
    bag_name = 'Bag0.bag'
    # initiate ros node
    rospy.init_node('record_data', anonymous=True)

    # initiate recorder (subscribers will be running all time but only write in bag if "is_recording=True")
    recorder = Recorder(bag_name)
    # start recording
    recorder.start_recording()
    
    # Manipulation task here .. or whatever code xD
    print("Some code started")
    print ("Waiting")
    rospy.sleep(5)
    print("some code ended")

    # stop recording
    recorder.stop_recording()

    # spin to keep the node alive
    rospy.spin()
