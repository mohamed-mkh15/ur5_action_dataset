#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import WrenchStamped
from arm_msgs.msg import ManipulatorState
import roslib; roslib.load_manifest('robotiq_2f_gripper_control')
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_input as inputMsg
import rosbag

class Recorder:
    def __init__(self, bag_name):
        # required rate in hz
        self.hz = 0.1
        # last received values
        self.camera0_color_info = None
        self.camera1_color_info= None
        self.camera0_color_compressed = None
        self.camera1_color_compressed = None
        self.camera0_depth_info = None
        self.camera1_depth_info= None
        self.camera0_depth_compressed = None
        self.camera1_depth_compressed = None
        self.arm_state = None
        self.gripper_state = None
        self.ft_sensor_state = None
        self.tf_static = None
        self.tf = None
        # start flags
        self.cam0 = False
        self.cam1 = False
        self.arm = False
        self.gripper = False
        self.ft_sensor = False
        # create bag
        self.bag_name = bag_name
        self.bag = None
        # initiate recording state
        self.is_recording = False
        # create subscribers
        self.sub_camera0_color_info = rospy.Subscriber('/camera1/color/camera_info', CameraInfo, self.callback_camera0_color_info, )
        self.sub_camera1_color_info = rospy.Subscriber('/camera1/color/image_raw/compressed', CompressedImage, self.callback_camera0_color_compressed)
        self.sub_camera0_color_compressed = rospy.Subscriber('/camera1/depth/camera_info', CameraInfo, self.callback_camera0_depth_info)
        self.sub_camera1_color_compressed = rospy.Subscriber('/camera1/aligned_depth_to_color/image_raw/compressed', CompressedImage, self.callback_camera0_depth_compressed)

        self.sub_camera0_depth_info = rospy.Subscriber('/camera2/color/camera_info', CameraInfo, self.callback_camera1_color_info)
        self.sub_camera1_depth_info = rospy.Subscriber('/camera2/color/image_raw/compressed', CompressedImage, self.callback_camera1_color_compressed)
        self.sub_camera0_depth_compressed = rospy.Subscriber('/camera2/depth/camera_info', CameraInfo, self.callback_camera1_depth_info)
        self.sub_camera1_depth_compressed = rospy.Subscriber('/camera2/aligned_depth_to_color/image_raw/compressed', CompressedImage, self.callback_camera1_depth_compressed)

        self.sub_arm_state = rospy.Subscriber('/ur_hardware_interface/arm_state', ManipulatorState, self.callback_arm_state)
        self.sub_gripper_state = rospy.Subscriber('/Robotiq2FGripperRobotInput', inputMsg.Robotiq2FGripper_robot_input, self.callback_gripper_state)
        self.sub_ft_sensor_state = rospy.Subscriber('/wrench', WrenchStamped, self.callback_ft_sensor_state)
        self.sub_tf_static = rospy.Subscriber('/tf', TFMessage, self.callback_tf)
        self.sub_tf = rospy.Subscriber('/tf_static', TFMessage, self.callback_tf_static)
        self.timer = rospy.Timer(rospy.Duration(self.hz), self.timer_callback)

    def print_state(self):
        print("Active status--> cam0: ", self.cam0," cam1: ", self.cam1, " arm: ", self.arm, " gripper: ", self.gripper, " ft_sensor: ", self.ft_sensor)

    def start_recording(self):
        if not self.is_recording:
            print("Satrted recording")
            self.bag = rosbag.Bag(self.bag_name, 'w')
            self.is_recording = True
    
    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.bag.close()
            self.bag = None
            print("Finished recording...bag saved")

    def callback_camera0_color_info(self ,message):
        self.camera0_color_info = message
        if (not self.cam0):
            self.cam0 = True

    def callback_camera1_color_info(self, message):
        self.camera1_color_info = message
        if (not self.cam1):
            self.cam1 = True

    def callback_camera0_color_compressed(self, message):
        self.camera0_color_compressed = message

    def callback_camera1_color_compressed(self, message):
        self.camera1_color_compressed = message

    def callback_camera0_depth_info(self, message):
        self.camera0_depth_info = message

    def callback_camera1_depth_info(self, message):
        self.camera1_depth_info = message

    def callback_camera0_depth_compressed(self, message):
        self.camera0_depth_compressed = message

    def callback_camera1_depth_compressed(self, message):
        self.camera1_depth_compressed = message

    def callback_arm_state(self, message):
        self.arm_state = message
        if (not self.arm):
            self.arm = True

    def callback_gripper_state(self, message):
        self.gripper_state = message
        if (not self.gripper):
            self.gripper = True

    def callback_ft_sensor_state(self, message):
        self.ft_sensor_state = message
        if (not self.ft_sensor):
            self.ft_sensor = True

    def callback_tf_static(self, message):
        self.tf_static = message

    def callback_tf(self, message):
        self.tf = message

    def timer_callback(self, event):
        if self.is_recording and self.cam0 and self.cam1 and self.arm and self.gripper and self.ft_sensor:
            self.bag.write('/sensor/camera/0/camera0/color/camera_info', self.camera0_color_info)
            self.bag.write('/sensor/camera/0/camera1/color/camera_info', self.camera1_color_info)
            self.bag.write('/sensor/camera/0/camera0/color/compressed', self.camera0_color_compressed)
            self.bag.write('/sensor/camera/0/camera1/color/compressed', self.camera1_color_compressed)
            self.bag.write('/sensor/camera/0/camera0/aligned_depth_to_color/camera_info', self.camera0_depth_info)
            self.bag.write('/sensor/camera/0/camera1/aligned_depth_to_color/camera_info', self.camera1_depth_info)
            self.bag.write('/sensor/camera/0/camera0/aligned_depth_to_color/compressed', self.camera0_depth_compressed)
            self.bag.write('/sensor/camera/0/camera1/aligned_depth_to_color/compressed', self.camera1_depth_compressed)
            self.bag.write('arm_state', self.arm_state)
            self.bag.write('gripper_state', self.gripper_state)
            self.bag.write('/sensor/ft_sensor/wrench_state', self.ft_sensor_state)
            self.bag.write('/sensor/camera/0/tf_static', self.tf_static)
            self.bag.write('/sensor/camera/0/tf', self.tf)
            # print("timer_callback -> done")

    def my_shutdown_handler(self):
        self.bag.close()
        print("shutdown time! .. Bag saved")