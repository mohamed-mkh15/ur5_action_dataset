Header header
float64[] q_target # an array of floating-point numbers representing the target joint positions
float64[] coeff_d # a floating-point number representing a differential coefficient for feedback loop
float64[] coeff_p # a floating-point number representing a proporsional coefficient for feedback loop
float64[] qd_target # an array of floating-point numbers representing the target joint velocities
float64[] i_target # an array of floating-point numbers representing the target joint currents
float64[] tau_target # an array of floating-point numbers representing the target joint torques
float64[] tool_vector_target # an array of floating-point numbers representing the tool vector
float64[] q_actual # an array of floating-point numbers representing the actual joint positions
float64[] qd_actual # an array of floating-point numbers representing the actual joint velocities
float64[] i_actual # an array of floating-point numbers representing the actual joint currents
float64[] tau_actual # an array of floating-point numbers representing the actual joint torques
float64[] tcp_force # an array of floating-point numbers representing the force applied to the tool center point (TCP)
float64[] tool_vector_actual # an array of floating-point numbers representing the tool vector
float64[] tcp_speed # an array of floating-point numbers representing the speed of the TCP
float64[] motor_temperatures # an array of floating-point numbers representing the temperatures of the motors
float64[] joint_modes # an array of floating-point numbers representing the modes of the joints
float64[] body_position # (unit: m), from own odometry in inertial frame, usually drift
float64[] euler_angles # (unit: rad), roll pitch yaw in stand mode, roll range:[-0.3, 0.3], pitch range:[-0.3, 0.3], yaw range:[-0.6, 0.6]
float64[2] body_velocity # (unit: m/s), forwardSpeed, sideSpeed in body frame, forwardSpeed range:[-0.8, 1.2], sideSpeed range: [-0.25, 0.25]
float64 body_height # (unit: m, default: 0.58m)
float64 body_width # (unit: m, default: )
float64 yaw_speed #(unit: rad/s), rotateSpeed in body frame
float64 controller_timer # a floating-point number representing the controller timer
float64[] qdd_target # an array of floating-point numbers representing the target joint accelerations
float64[] qdd_actual # an array of floating-point numbers representing the actual joint accelerations
float64[] tool_acc_values # an array of floating-point numbers representing the tool acceleration values
float64 robot_mode # a floating-point number representing the current robot mode
float64 digital_input_bits # a floating-point number representing the state of the digital input bits
float64 test_value # a floating-point number representing a test value