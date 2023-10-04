;; Auto-generated. Do not edit!


(when (boundp 'arm_msgs::ManipulatorState)
  (if (not (find-package "ARM_MSGS"))
    (make-package "ARM_MSGS"))
  (shadow 'ManipulatorState (find-package "ARM_MSGS")))
(unless (find-package "ARM_MSGS::MANIPULATORSTATE")
  (make-package "ARM_MSGS::MANIPULATORSTATE"))

(in-package "ROS")
;;//! \htmlinclude ManipulatorState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass arm_msgs::ManipulatorState
  :super ros::object
  :slots (_header _q_target _qd_target _i_target _m_target _tau_target _tool_vector_target _q_actual _qd_actual _i_actual _tau_actual _tcp_force _tool_vector_actual _motor_temperatures _joint_modes _controller_timer _qdd_target _tool_acc_values _robot_mode _test_value _m_actual _digital_input_bits _tcp_speed_target _tcp_speed_actual ))

(defmethod arm_msgs::ManipulatorState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:q_target __q_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:qd_target __qd_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:i_target __i_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:m_target __m_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tau_target __tau_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_vector_target __tool_vector_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:q_actual __q_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:qd_actual __qd_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:i_actual __i_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tau_actual __tau_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tcp_force __tcp_force) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_vector_actual __tool_vector_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:motor_temperatures __motor_temperatures) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:joint_modes __joint_modes) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:controller_timer __controller_timer) 0.0)
    ((:qdd_target __qdd_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_acc_values __tool_acc_values) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:robot_mode __robot_mode) 0.0)
    ((:test_value __test_value) 0.0)
    ((:m_actual __m_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:digital_input_bits __digital_input_bits) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tcp_speed_target __tcp_speed_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tcp_speed_actual __tcp_speed_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _q_target __q_target)
   (setq _qd_target __qd_target)
   (setq _i_target __i_target)
   (setq _m_target __m_target)
   (setq _tau_target __tau_target)
   (setq _tool_vector_target __tool_vector_target)
   (setq _q_actual __q_actual)
   (setq _qd_actual __qd_actual)
   (setq _i_actual __i_actual)
   (setq _tau_actual __tau_actual)
   (setq _tcp_force __tcp_force)
   (setq _tool_vector_actual __tool_vector_actual)
   (setq _motor_temperatures __motor_temperatures)
   (setq _joint_modes __joint_modes)
   (setq _controller_timer (float __controller_timer))
   (setq _qdd_target __qdd_target)
   (setq _tool_acc_values __tool_acc_values)
   (setq _robot_mode (float __robot_mode))
   (setq _test_value (float __test_value))
   (setq _m_actual __m_actual)
   (setq _digital_input_bits __digital_input_bits)
   (setq _tcp_speed_target __tcp_speed_target)
   (setq _tcp_speed_actual __tcp_speed_actual)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:q_target
   (&optional __q_target)
   (if __q_target (setq _q_target __q_target)) _q_target)
  (:qd_target
   (&optional __qd_target)
   (if __qd_target (setq _qd_target __qd_target)) _qd_target)
  (:i_target
   (&optional __i_target)
   (if __i_target (setq _i_target __i_target)) _i_target)
  (:m_target
   (&optional __m_target)
   (if __m_target (setq _m_target __m_target)) _m_target)
  (:tau_target
   (&optional __tau_target)
   (if __tau_target (setq _tau_target __tau_target)) _tau_target)
  (:tool_vector_target
   (&optional __tool_vector_target)
   (if __tool_vector_target (setq _tool_vector_target __tool_vector_target)) _tool_vector_target)
  (:q_actual
   (&optional __q_actual)
   (if __q_actual (setq _q_actual __q_actual)) _q_actual)
  (:qd_actual
   (&optional __qd_actual)
   (if __qd_actual (setq _qd_actual __qd_actual)) _qd_actual)
  (:i_actual
   (&optional __i_actual)
   (if __i_actual (setq _i_actual __i_actual)) _i_actual)
  (:tau_actual
   (&optional __tau_actual)
   (if __tau_actual (setq _tau_actual __tau_actual)) _tau_actual)
  (:tcp_force
   (&optional __tcp_force)
   (if __tcp_force (setq _tcp_force __tcp_force)) _tcp_force)
  (:tool_vector_actual
   (&optional __tool_vector_actual)
   (if __tool_vector_actual (setq _tool_vector_actual __tool_vector_actual)) _tool_vector_actual)
  (:motor_temperatures
   (&optional __motor_temperatures)
   (if __motor_temperatures (setq _motor_temperatures __motor_temperatures)) _motor_temperatures)
  (:joint_modes
   (&optional __joint_modes)
   (if __joint_modes (setq _joint_modes __joint_modes)) _joint_modes)
  (:controller_timer
   (&optional __controller_timer)
   (if __controller_timer (setq _controller_timer __controller_timer)) _controller_timer)
  (:qdd_target
   (&optional __qdd_target)
   (if __qdd_target (setq _qdd_target __qdd_target)) _qdd_target)
  (:tool_acc_values
   (&optional __tool_acc_values)
   (if __tool_acc_values (setq _tool_acc_values __tool_acc_values)) _tool_acc_values)
  (:robot_mode
   (&optional __robot_mode)
   (if __robot_mode (setq _robot_mode __robot_mode)) _robot_mode)
  (:test_value
   (&optional __test_value)
   (if __test_value (setq _test_value __test_value)) _test_value)
  (:m_actual
   (&optional __m_actual)
   (if __m_actual (setq _m_actual __m_actual)) _m_actual)
  (:digital_input_bits
   (&optional __digital_input_bits)
   (if __digital_input_bits (setq _digital_input_bits __digital_input_bits)) _digital_input_bits)
  (:tcp_speed_target
   (&optional __tcp_speed_target)
   (if __tcp_speed_target (setq _tcp_speed_target __tcp_speed_target)) _tcp_speed_target)
  (:tcp_speed_actual
   (&optional __tcp_speed_actual)
   (if __tcp_speed_actual (setq _tcp_speed_actual __tcp_speed_actual)) _tcp_speed_actual)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64[] _q_target
    (* 8    (length _q_target)) 4
    ;; float64[] _qd_target
    (* 8    (length _qd_target)) 4
    ;; float64[] _i_target
    (* 8    (length _i_target)) 4
    ;; float64[] _m_target
    (* 8    (length _m_target)) 4
    ;; float64[] _tau_target
    (* 8    (length _tau_target)) 4
    ;; float64[] _tool_vector_target
    (* 8    (length _tool_vector_target)) 4
    ;; float64[] _q_actual
    (* 8    (length _q_actual)) 4
    ;; float64[] _qd_actual
    (* 8    (length _qd_actual)) 4
    ;; float64[] _i_actual
    (* 8    (length _i_actual)) 4
    ;; float64[] _tau_actual
    (* 8    (length _tau_actual)) 4
    ;; float64[] _tcp_force
    (* 8    (length _tcp_force)) 4
    ;; float64[] _tool_vector_actual
    (* 8    (length _tool_vector_actual)) 4
    ;; float64[] _motor_temperatures
    (* 8    (length _motor_temperatures)) 4
    ;; float64[] _joint_modes
    (* 8    (length _joint_modes)) 4
    ;; float64 _controller_timer
    8
    ;; float64[] _qdd_target
    (* 8    (length _qdd_target)) 4
    ;; float64[] _tool_acc_values
    (* 8    (length _tool_acc_values)) 4
    ;; float64 _robot_mode
    8
    ;; float64 _test_value
    8
    ;; float64[] _m_actual
    (* 8    (length _m_actual)) 4
    ;; float64[] _digital_input_bits
    (* 8    (length _digital_input_bits)) 4
    ;; float64[] _tcp_speed_target
    (* 8    (length _tcp_speed_target)) 4
    ;; float64[] _tcp_speed_actual
    (* 8    (length _tcp_speed_actual)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64[] _q_target
     (write-long (length _q_target) s)
     (dotimes (i (length _q_target))
       (sys::poke (elt _q_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _qd_target
     (write-long (length _qd_target) s)
     (dotimes (i (length _qd_target))
       (sys::poke (elt _qd_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _i_target
     (write-long (length _i_target) s)
     (dotimes (i (length _i_target))
       (sys::poke (elt _i_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _m_target
     (write-long (length _m_target) s)
     (dotimes (i (length _m_target))
       (sys::poke (elt _m_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tau_target
     (write-long (length _tau_target) s)
     (dotimes (i (length _tau_target))
       (sys::poke (elt _tau_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tool_vector_target
     (write-long (length _tool_vector_target) s)
     (dotimes (i (length _tool_vector_target))
       (sys::poke (elt _tool_vector_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _q_actual
     (write-long (length _q_actual) s)
     (dotimes (i (length _q_actual))
       (sys::poke (elt _q_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _qd_actual
     (write-long (length _qd_actual) s)
     (dotimes (i (length _qd_actual))
       (sys::poke (elt _qd_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _i_actual
     (write-long (length _i_actual) s)
     (dotimes (i (length _i_actual))
       (sys::poke (elt _i_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tau_actual
     (write-long (length _tau_actual) s)
     (dotimes (i (length _tau_actual))
       (sys::poke (elt _tau_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tcp_force
     (write-long (length _tcp_force) s)
     (dotimes (i (length _tcp_force))
       (sys::poke (elt _tcp_force i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tool_vector_actual
     (write-long (length _tool_vector_actual) s)
     (dotimes (i (length _tool_vector_actual))
       (sys::poke (elt _tool_vector_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _motor_temperatures
     (write-long (length _motor_temperatures) s)
     (dotimes (i (length _motor_temperatures))
       (sys::poke (elt _motor_temperatures i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _joint_modes
     (write-long (length _joint_modes) s)
     (dotimes (i (length _joint_modes))
       (sys::poke (elt _joint_modes i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _controller_timer
       (sys::poke _controller_timer (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _qdd_target
     (write-long (length _qdd_target) s)
     (dotimes (i (length _qdd_target))
       (sys::poke (elt _qdd_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tool_acc_values
     (write-long (length _tool_acc_values) s)
     (dotimes (i (length _tool_acc_values))
       (sys::poke (elt _tool_acc_values i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _robot_mode
       (sys::poke _robot_mode (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _test_value
       (sys::poke _test_value (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _m_actual
     (write-long (length _m_actual) s)
     (dotimes (i (length _m_actual))
       (sys::poke (elt _m_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _digital_input_bits
     (write-long (length _digital_input_bits) s)
     (dotimes (i (length _digital_input_bits))
       (sys::poke (elt _digital_input_bits i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tcp_speed_target
     (write-long (length _tcp_speed_target) s)
     (dotimes (i (length _tcp_speed_target))
       (sys::poke (elt _tcp_speed_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tcp_speed_actual
     (write-long (length _tcp_speed_actual) s)
     (dotimes (i (length _tcp_speed_actual))
       (sys::poke (elt _tcp_speed_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64[] _q_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _q_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _q_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _qd_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qd_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _qd_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _i_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _i_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _i_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _m_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _m_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _m_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tau_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tau_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tau_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tool_vector_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tool_vector_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tool_vector_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _q_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _q_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _q_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _qd_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qd_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _qd_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _i_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _i_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _i_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tau_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tau_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tau_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tcp_force
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tcp_force (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tcp_force i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tool_vector_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tool_vector_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tool_vector_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _motor_temperatures
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _motor_temperatures (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _motor_temperatures i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _joint_modes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joint_modes (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _joint_modes i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _controller_timer
     (setq _controller_timer (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _qdd_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qdd_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _qdd_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tool_acc_values
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tool_acc_values (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tool_acc_values i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _robot_mode
     (setq _robot_mode (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _test_value
     (setq _test_value (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _m_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _m_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _m_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _digital_input_bits
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _digital_input_bits (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _digital_input_bits i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tcp_speed_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tcp_speed_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tcp_speed_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _tcp_speed_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tcp_speed_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tcp_speed_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get arm_msgs::ManipulatorState :md5sum-) "30e728ca616a11ea04e008e82f09e713")
(setf (get arm_msgs::ManipulatorState :datatype-) "arm_msgs/ManipulatorState")
(setf (get arm_msgs::ManipulatorState :definition-)
      "Header header
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


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :arm_msgs/ManipulatorState "30e728ca616a11ea04e008e82f09e713")


