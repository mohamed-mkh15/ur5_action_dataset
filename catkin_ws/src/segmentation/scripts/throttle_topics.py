#!/usr/bin/env python

import rospy
# from sensor_msgs.msg import PointCloud2
# from sensor_msgs.msg import Image
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import WrenchStamped
from arm_msgs.msg import ManipulatorState
import roslib; roslib.load_manifest('robotiq_2f_gripper_control')
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_input as inputMsg

# last_data = ""
camera0_color_info = None
camera1_color_info= None
camera0_color_compressed = None
camera1_color_compressed = None
camera0_depth_info = None
camera1_depth_info= None
camera0_depth_compressed = None
camera1_depth_compressed = None
arm_state = None
gripper_state = None
ft_sensor_state = None
tf_static = None
tf = None
# pcl = None

cam0 = False
cam1 = False
arm = False
gripper = False
ft_sensor = False

pub_camera0_color_info = rospy.Publisher('/sensor/camera/0/camera0/color/camera_info', CameraInfo,  queue_size=10)
pub_camera1_color_info = rospy.Publisher('/sensor/camera/0/camera1/color/camera_info', CameraInfo,  queue_size=10)
pub_camera0_color_compressed = rospy.Publisher('/sensor/camera/0/camera0/color/compressed', CompressedImage,  queue_size=10)
pub_camera1_color_compressed = rospy.Publisher('/sensor/camera/0/camera1/color/compressed', CompressedImage,  queue_size=10)

pub_camera0_depth_info = rospy.Publisher('/sensor/camera/0/camera0/aligned_depth_to_color/camera_info', CameraInfo,  queue_size=10)
pub_camera1_depth_info = rospy.Publisher('/sensor/camera/0/camera1/aligned_depth_to_color/camera_info', CameraInfo,  queue_size=10)
pub_camera0_depth_compressed = rospy.Publisher('/sensor/camera/0/camera0/aligned_depth_to_color/compressed', CompressedImage,  queue_size=10)
pub_camera1_depth_compressed = rospy.Publisher('/sensor/camera/0/camera1/aligned_depth_to_color/compressed', CompressedImage,  queue_size=10)

pub_arm_sate = rospy.Publisher('/state/arm/0/arm_state', ManipulatorState,  queue_size=10)
pub_gripper_state = rospy.Publisher('/state/arm/0/gripper_state', inputMsg.Robotiq2FGripper_robot_input,  queue_size=10)
pub_ft_sensor_state = rospy.Publisher('/sensor/ft_sensor/wrench_state', WrenchStamped,  queue_size=10)

pub_tf_static= rospy.Publisher('/sensor/camera/0/tf_static', TFMessage,  queue_size=10)
pub_tf = rospy.Publisher('/sensor/camera/0/tf', TFMessage,  queue_size=10)
# pub_pcl = rospy.Publisher('/throttle/pcl', PointCloud2,  queue_size=10)


def callback_camera0_color_info(data):
    global cam0, camera0_color_info 
    camera0_color_info = data
    if (not cam0):
        cam0 = True

def callback_camera1_color_info(data):
    global cam1, camera1_color_info 
    camera1_color_info = data
    if (not cam1):
        cam1 = True

def callback_camera0_color_compressed(data):
    global camera0_color_compressed 
    camera0_color_compressed = data

def callback_camera1_color_compressed(data):
    global camera1_color_compressed 
    camera1_color_compressed = data

def callback_camera0_depth_info(data):
    global camera0_depth_info 
    camera0_depth_info = data

def callback_camera1_depth_info(data):
    global camera1_depth_info 
    camera1_depth_info = data

def callback_camera0_depth_compressed(data):
    global camera0_depth_compressed 
    camera0_depth_compressed = data

def callback_camera1_depth_compressed(data):
    global camera1_depth_compressed 
    camera1_depth_compressed = data

def callback_arm_state(data):
    global arm, arm_state 
    arm_state = data
    if (not arm):
        arm = True

def callback_gripper_state(data):
    global gripper, gripper_state 
    gripper_state = data
    if (not gripper):
        gripper = True

def callback_ft_sensor_state(data):
    global ft_sensor, ft_sensor_state
    ft_sensor_state = data
    if (not ft_sensor):
        ft_sensor = True

def callback_tf_static(data):
    global tf_static 
    tf_static = data

def callback_tf(data):
    global tf 
    tf = data

# def callback_pcl(data):
#     global started2, pcl 
#     pcl = data
#     if (not started2):
#         started2 = True

def timer_callback(event):
    global cam0, cam1, arm, gripper, ft_sensor
    global pub_camera0_color_info, pub_camera0_color_compressed, pub_camera0_depth_info, pub_camera0_depth_compressed
    global pub_camera1_color_info, pub_camera1_color_compressed, pub_camera1_depth_info, pub_camera1_depth_compressed
    global pub_arm_sate, pub_gripper_state, pub_ft_sensor_state
    global camera0_color_info, camera0_color_compressed, camera0_depth_info, camera0_depth_compressed
    global camera1_color_info, camera1_color_compressed, camera1_depth_info, camera1_depth_compressed
    global arm_state, gripper_state, ft_sensor_state, tf, tf_static

    print("Active status--> cam0: ", cam0," cam1: ", cam1, " arm: ", arm, " gripper: ", gripper, " ft_sensor: ", ft_sensor)
    if cam0 and cam1 and arm and gripper and ft_sensor:
        pub_camera0_color_info.publish(camera0_color_info)
        pub_camera1_color_info.publish(camera1_color_info)
        pub_camera0_color_compressed.publish(camera0_color_compressed)
        pub_camera1_color_compressed.publish(camera1_color_compressed)

        pub_camera0_depth_info.publish(camera0_depth_info)
        pub_camera1_depth_info.publish(camera1_depth_info)
        pub_camera0_depth_compressed.publish(camera0_depth_compressed)
        pub_camera1_depth_compressed.publish(camera1_depth_compressed)

        pub_arm_sate.publish(arm_state)
        pub_gripper_state.publish(gripper_state)
        pub_ft_sensor_state.publish(ft_sensor_state)
        pub_tf.publish(tf)
        pub_tf_static.publish(tf_static)
        print("Last message published")


def main():

    rospy.init_node('throttle', anonymous=True)
    rospy.Subscriber('/camera1/color/camera_info', CameraInfo, callback_camera0_color_info)
    rospy.Subscriber('/camera1/color/image_raw/compressed', CompressedImage, callback_camera0_color_compressed)
    rospy.Subscriber('/camera1/depth/camera_info', CameraInfo, callback_camera0_depth_info)
    rospy.Subscriber('/camera1/aligned_depth_to_color/image_raw/compressed', CompressedImage, callback_camera0_depth_compressed)

    rospy.Subscriber('/camera2/color/camera_info', CameraInfo, callback_camera1_color_info)
    rospy.Subscriber('/camera2/color/image_raw/compressed', CompressedImage, callback_camera1_color_compressed)
    rospy.Subscriber('/camera2/depth/camera_info', CameraInfo, callback_camera1_depth_info)
    rospy.Subscriber('/camera2/aligned_depth_to_color/image_raw/compressed', CompressedImage, callback_camera1_depth_compressed)

    # rospy.Subscriber('/camera/depth_registered/points', PointCloud2, callback_pcl)
    rospy.Subscriber('/ur_hardware_interface/arm_state', ManipulatorState, callback_arm_state)
    rospy.Subscriber('/Robotiq2FGripperRobotInput', inputMsg.Robotiq2FGripper_robot_input, callback_gripper_state)
    rospy.Subscriber('/wrench', WrenchStamped, callback_ft_sensor_state)
    rospy.Subscriber('/tf', TFMessage, callback_tf)
    rospy.Subscriber('/tf_static', TFMessage, callback_tf_static)

    timer = rospy.Timer(rospy.Duration(0.1), timer_callback)

    rospy.spin()    
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()