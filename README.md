# ur_robotic arm_action_dataset

This project aims at recording dataset for object recognetion and manipulation using realsense D435i rgbd camera and ur5 robotic arm with robotiq 2f gripper and force torque sensor. 


## Installation
You can either download this whole catkin_ws and just build it (install missing pkgs) or you can just download the segmentation pkg from this repo and then install the other pkgs one by one as following:

### 1- Realsense camera 
Install relasense wraper for ROS
$sudo apt-get install ros-melodic-realsense2-camera

Then you can run the driver using:
$roslaunch realsense2_camera rs_rgbd.launch

To check the amera publishing rate and image size ..etc (change video0 if needed.. use $ v4l2-ctl --list-devices )
$v4l2-ctl -d /dev/video0 --list-formats-ext

I got error so tried installing this:
sudo apt install ros-melodic-rgbd-launch


### 2- Robotiq Gripper 
Run roscore:
$roscore

check which port for the gripper
$dmesg | grep tty

make sure user have writing authority

Run the device in a separate terminal:
$rosrun robotiq_2f_gripper_control Robotiq2FGripperRtuNode.py /dev/ttyUSB0 #USB0 might change in ur case

run the listener if needed
$rosrun robotiq_2f_gripper_control Robotiq2FGrierStatusListener.py

run the controller if needed (don't forget to activate first... and just write the letter corresponding toe the command + enter)
$rosrun robotiq_2f_gripper_control Robotiq2FGripperSimpleController.py


### 3- Connect to the ur5 robot
run driver node (UR5)
$roslaunch ur_robot_driver ur5_bringup.launch robot_ip:=192.168.88.206 #check ur robot ip


### 4- or you can just lunch all of them at once from the drivers.launch in segmentation pkg.
