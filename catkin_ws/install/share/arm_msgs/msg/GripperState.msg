Header header
float64[] coeff_p # a floating-point number representing a proporsional coefficient for feedback loop
uint8[] gripper_cmd # sequence of bits which representing the command to the gripper
uint8[] gripper_status # sequence of bits which representing the status of the gripper
float32[] ee_ft # 3 forces and 3 torques on the end-effector with additinal sensor
float64[] gripper_joints # a floating-point number representing an angle of gripper
float64 gripper_torque # a floating-point number representing a torque value on gripper joint
float64[] coeff_d # a floating-point number representing a differential coefficient for feedback loop
float64[] gripper_speed # a floating-point number representing velocity of the gripper joints.