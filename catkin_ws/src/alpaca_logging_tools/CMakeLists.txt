cmake_minimum_required(VERSION 3.0.2)
project(logging_tools)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  sensor_msgs
  geometry_msgs
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
  geometry_msgs
)

catkin_package(
   CATKIN_DEPENDS rospy std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)