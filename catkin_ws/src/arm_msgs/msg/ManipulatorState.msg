Header header
float64[] q_target # an array of floating-point numbers representing the target joint positions
float64[] qd_target # an array of floating-point numbers representing the target joint velocities
float64[] i_target # an array of floating-point numbers representing the target joint currents
float64[] m_target # an array of floating-point numbers representing the target joint moments
float64[] tau_target # an array of floating-point numbers representing the target joint torques
float64[] tool_vector_target # an array of floating-point numbers representing the tool vector
float64[] q_actual # an array of floating-point numbers representing the actual joint positions
float64[] qd_actual # an array of floating-point numbers representing the actual joint velocities
float64[] i_actual # an array of floating-point numbers representing the actual joint currents
float64[] tau_actual # an array of floating-point numbers representing the actual joint torques
float64[] tcp_force # an array of floating-point numbers representing the force applied to the tool center point (TCP)
float64[] tool_vector_actual # an array of floating-point numbers representing the tool vector
float64[] motor_temperatures # an array of floating-point numbers representing the temperatures of the motors
float64[] joint_modes # an array of floating-point numbers representing the modes of the joints
float64 controller_timer # a floating-point number representing the controller timer
float64[] qdd_target # an array of floating-point numbers representing the target joint accelerations
# float64[] qdd_actual # an array of floating-point numbers representing the actual joint accelerations
float64[] tool_acc_values # an array of floating-point numbers representing the tool acceleration values
float64 robot_mode # a floating-point number representing the current robot mode
float64 test_value # a floating-point number representing a test value

# edit
float64[] m_actual  # an array of floating-point numbers representing the actual joint moments
float64[] digital_input_bits # a floating-point number representing the state of the digital input bits
float64[] tcp_speed_target # an array of floating-point numbers representing the target speed of the TCP
float64[] tcp_speed_actual # an array of floating-point numbers representing the actual speed of the TCP

