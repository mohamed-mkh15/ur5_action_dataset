#! /usr/bin/env python3

import subprocess
import rospy
from arm_msgs.msg import ManipulatorState, GripperState, LegState
from threading import Thread
import message_filters
from copy import deepcopy
from random import random

from control_msgs.msg import FollowJointTrajectoryActionFeedback
from geometry_msgs.msg import WrenchStamped
from sensor_msgs.msg import JointState
from ur_msgs.msg import ToolDataMsg, IOStates
from ur_dashboard_msgs.msg import RobotMode
from tf2_msgs.msg import TFMessage


def run_relays(relay_topics):
    subprocesses_list = []
    params = ['_unreliable:=False', '_lazy:=True']
    for original, duplicate in relay_topics.items():
        process = subprocess.Popen(['rosrun', 'topic_tools', 'relay', original, duplicate, *params])
        subprocesses_list.append(process)
    return subprocesses_list


class ArmStatesSub:
    def __init__(self, parent_topic='/arm/1'):
        self._parent_topic = parent_topic
        self._traj_controller_last_msg = FollowJointTrajectoryActionFeedback()
        self._robot_state = {
            'robot_mode': 0,
            'digital_input_bits': [0] * 22
        }
        # self._sync_subscribe()
        self._advertise()
        rospy.Subscriber('/scaled_pos_joint_traj_controller/follow_joint_trajectory/feedback', FollowJointTrajectoryActionFeedback, self._traj_controller_cb)
        rospy.Subscriber('ur_hardware_interface/robot_mode', RobotMode, self._robot_mode_cb)
        rospy.Subscriber('ur_hardware_interface/io_states', IOStates, self._robot_io_cb)
        rospy.Subscriber(f'{self._parent_topic}/robot_state', ManipulatorState, self._manipulator_states_cb)
        
    def _advertise(self):
        self._arm_state_topic = rospy.Publisher(f"/state{self._parent_topic}/arm_state", ManipulatorState, queue_size=1)

    # def _sync_subscribe(self):
    #     joint_states_sub = message_filters.Subscriber(f'{self._parent_topic}/joint_states', JointState)
    #     wrench_sub = message_filters.Subscriber(f'{self._parent_topic}/wrench', WrenchStamped)
    #     manipulator_sub = message_filters.Subscriber(f'{self._parent_topic}/robot_state', ManipulatorState)
    #     ts = message_filters.ApproximateTimeSynchronizer([wrench_sub, joint_states_sub, manipulator_sub], 5, 0.5)
    #     ts.registerCallback(self._manipulator_states_cb)

    def _manipulator_states_cb(self, manipulator_state_msg):
        header = rospy.Header()
        header.frame_id = self._parent_topic
        header.stamp = manipulator_state_msg.header.stamp
        # desired = self.traj_controller_msg.feedback.desired
        # tcp_force = list([getattr(wrench_msg.wrench.force, axis) for axis in ['x', 'y', 'z']])
        # tcp_force.extend([getattr(wrench_msg.wrench.torque, axis) for axis in ['x', 'y', 'z']])
        arm_state_msg = deepcopy(manipulator_state_msg)
        change_fields = {'header': header,
                         'test_value': random(),
                         'digital_input_bits': self._robot_state['digital_input_bits']}
        for field, value in change_fields.items():
            setattr(arm_state_msg, field, value)
        self._arm_state_topic.publish(arm_state_msg)
    
    @property
    def traj_controller_msg(self):
        if rospy.Time.now() - self._traj_controller_last_msg.header.stamp < rospy.Duration(0.1):
            # if less than 0.1 sec
            return self._traj_controller_last_msg
        else:
            traj_controller_msg = deepcopy(self._traj_controller_last_msg)
            desired = traj_controller_msg.feedback.desired
            desired.velocities = [0] * 6
            desired.accelerations = [0] * 6
            return traj_controller_msg

    def _traj_controller_cb(self, controller_msg):
        self._traj_controller_last_msg = controller_msg
    
    def _robot_mode_cb(self, robot_mode):
        self._robot_state['robot_mode'] = robot_mode.mode

    def _robot_io_cb(self, io_state):
        states = []
        for digital_in in io_state.digital_in_states:
            states.append(digital_in.state)
        for digital_out in io_state.digital_out_states:
            states.append(digital_out.state)
        states.extend(io_state.flag_states)
        for analog_in in io_state.analog_in_states:
            states.append(analog_in.state)
        for analog_out in io_state.analog_out_states:
            states.append(analog_out.state)
        self._robot_state['digital_input_bits'] = list(map(float, states))
        


if __name__ == "__main__":
    relay_topics = {
        '/joint_states': '/arm/1/joint_states',
        '/wrench': '/arm/1/wrench',
        '/ur_hardware_interface/arm_state': '/arm/1/robot_state',
        # '/camera/color/camera_info': '/sensor/camera/1/color/camera_info',
        # '/camera/color/image_raw': '/sensor/camera/1/color/image_raw',
        # '/camera/color/image_raw/compressed': '/sensor/camera/1/color/image_raw/compressed',
        # '/camera/depth/camera_info': '/sensor/camera/1/depth/camera_info',
        # '/camera/depth/image_rect_raw': '/sensor/camera/1/depth/image_rect_raw',
        # '/camera/depth/image_rect_raw/compressed': '/sensor/camera/1/depth/image_rect_raw/compressed',
        # '/camera/depth/image_rect_raw/compressedDepth': '/sensor/camera/1/depth/image_rect_raw/compressedDepth',
        # '/camera/depth/color/points': '/sensor/camera/1/depth/color/points',
        # '/camera/aligned_depth_to_color/camera_info': '/sensor/camera/1/aligned_depth_to_color/camera_info',
        # '/camera/aligned_depth_to_color/image_raw': '/sensor/camera/1/aligned_depth_to_color/image_raw',
        # '/camera/aligned_depth_to_color/image_raw/compressed': '/sensor/camera/1/aligned_depth_to_color/image_raw/compressed'
    }
    rospy.init_node('republisher_node')
    run_relays(relay_topics)
    arm_states_sub = ArmStatesSub('/arm/1')
    rospy.spin()