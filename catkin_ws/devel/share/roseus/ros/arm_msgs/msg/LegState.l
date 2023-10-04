;; Auto-generated. Do not edit!


(when (boundp 'arm_msgs::LegState)
  (if (not (find-package "ARM_MSGS"))
    (make-package "ARM_MSGS"))
  (shadow 'LegState (find-package "ARM_MSGS")))
(unless (find-package "ARM_MSGS::LEGSTATE")
  (make-package "ARM_MSGS::LEGSTATE"))

(in-package "ROS")
;;//! \htmlinclude LegState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass arm_msgs::LegState
  :super ros::object
  :slots (_header _q_target _coeff_d _coeff_p _qd_target _i_target _tau_target _tool_vector_target _q_actual _qd_actual _i_actual _tau_actual _tcp_force _tool_vector_actual _tcp_speed _motor_temperatures _joint_modes _body_position _euler_angles _body_velocity _body_height _body_width _yaw_speed _controller_timer _qdd_target _qdd_actual _tool_acc_values _robot_mode _digital_input_bits _test_value ))

(defmethod arm_msgs::LegState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:q_target __q_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:coeff_d __coeff_d) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:coeff_p __coeff_p) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:qd_target __qd_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:i_target __i_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tau_target __tau_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_vector_target __tool_vector_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:q_actual __q_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:qd_actual __qd_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:i_actual __i_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tau_actual __tau_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tcp_force __tcp_force) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_vector_actual __tool_vector_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tcp_speed __tcp_speed) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:motor_temperatures __motor_temperatures) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:joint_modes __joint_modes) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:body_position __body_position) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:euler_angles __euler_angles) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:body_velocity __body_velocity) (make-array 2 :initial-element 0.0 :element-type :float))
    ((:body_height __body_height) 0.0)
    ((:body_width __body_width) 0.0)
    ((:yaw_speed __yaw_speed) 0.0)
    ((:controller_timer __controller_timer) 0.0)
    ((:qdd_target __qdd_target) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:qdd_actual __qdd_actual) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tool_acc_values __tool_acc_values) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:robot_mode __robot_mode) 0.0)
    ((:digital_input_bits __digital_input_bits) 0.0)
    ((:test_value __test_value) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _q_target __q_target)
   (setq _coeff_d __coeff_d)
   (setq _coeff_p __coeff_p)
   (setq _qd_target __qd_target)
   (setq _i_target __i_target)
   (setq _tau_target __tau_target)
   (setq _tool_vector_target __tool_vector_target)
   (setq _q_actual __q_actual)
   (setq _qd_actual __qd_actual)
   (setq _i_actual __i_actual)
   (setq _tau_actual __tau_actual)
   (setq _tcp_force __tcp_force)
   (setq _tool_vector_actual __tool_vector_actual)
   (setq _tcp_speed __tcp_speed)
   (setq _motor_temperatures __motor_temperatures)
   (setq _joint_modes __joint_modes)
   (setq _body_position __body_position)
   (setq _euler_angles __euler_angles)
   (setq _body_velocity __body_velocity)
   (setq _body_height (float __body_height))
   (setq _body_width (float __body_width))
   (setq _yaw_speed (float __yaw_speed))
   (setq _controller_timer (float __controller_timer))
   (setq _qdd_target __qdd_target)
   (setq _qdd_actual __qdd_actual)
   (setq _tool_acc_values __tool_acc_values)
   (setq _robot_mode (float __robot_mode))
   (setq _digital_input_bits (float __digital_input_bits))
   (setq _test_value (float __test_value))
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
  (:coeff_d
   (&optional __coeff_d)
   (if __coeff_d (setq _coeff_d __coeff_d)) _coeff_d)
  (:coeff_p
   (&optional __coeff_p)
   (if __coeff_p (setq _coeff_p __coeff_p)) _coeff_p)
  (:qd_target
   (&optional __qd_target)
   (if __qd_target (setq _qd_target __qd_target)) _qd_target)
  (:i_target
   (&optional __i_target)
   (if __i_target (setq _i_target __i_target)) _i_target)
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
  (:tcp_speed
   (&optional __tcp_speed)
   (if __tcp_speed (setq _tcp_speed __tcp_speed)) _tcp_speed)
  (:motor_temperatures
   (&optional __motor_temperatures)
   (if __motor_temperatures (setq _motor_temperatures __motor_temperatures)) _motor_temperatures)
  (:joint_modes
   (&optional __joint_modes)
   (if __joint_modes (setq _joint_modes __joint_modes)) _joint_modes)
  (:body_position
   (&optional __body_position)
   (if __body_position (setq _body_position __body_position)) _body_position)
  (:euler_angles
   (&optional __euler_angles)
   (if __euler_angles (setq _euler_angles __euler_angles)) _euler_angles)
  (:body_velocity
   (&optional __body_velocity)
   (if __body_velocity (setq _body_velocity __body_velocity)) _body_velocity)
  (:body_height
   (&optional __body_height)
   (if __body_height (setq _body_height __body_height)) _body_height)
  (:body_width
   (&optional __body_width)
   (if __body_width (setq _body_width __body_width)) _body_width)
  (:yaw_speed
   (&optional __yaw_speed)
   (if __yaw_speed (setq _yaw_speed __yaw_speed)) _yaw_speed)
  (:controller_timer
   (&optional __controller_timer)
   (if __controller_timer (setq _controller_timer __controller_timer)) _controller_timer)
  (:qdd_target
   (&optional __qdd_target)
   (if __qdd_target (setq _qdd_target __qdd_target)) _qdd_target)
  (:qdd_actual
   (&optional __qdd_actual)
   (if __qdd_actual (setq _qdd_actual __qdd_actual)) _qdd_actual)
  (:tool_acc_values
   (&optional __tool_acc_values)
   (if __tool_acc_values (setq _tool_acc_values __tool_acc_values)) _tool_acc_values)
  (:robot_mode
   (&optional __robot_mode)
   (if __robot_mode (setq _robot_mode __robot_mode)) _robot_mode)
  (:digital_input_bits
   (&optional __digital_input_bits)
   (if __digital_input_bits (setq _digital_input_bits __digital_input_bits)) _digital_input_bits)
  (:test_value
   (&optional __test_value)
   (if __test_value (setq _test_value __test_value)) _test_value)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64[] _q_target
    (* 8    (length _q_target)) 4
    ;; float64[] _coeff_d
    (* 8    (length _coeff_d)) 4
    ;; float64[] _coeff_p
    (* 8    (length _coeff_p)) 4
    ;; float64[] _qd_target
    (* 8    (length _qd_target)) 4
    ;; float64[] _i_target
    (* 8    (length _i_target)) 4
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
    ;; float64[] _tcp_speed
    (* 8    (length _tcp_speed)) 4
    ;; float64[] _motor_temperatures
    (* 8    (length _motor_temperatures)) 4
    ;; float64[] _joint_modes
    (* 8    (length _joint_modes)) 4
    ;; float64[] _body_position
    (* 8    (length _body_position)) 4
    ;; float64[] _euler_angles
    (* 8    (length _euler_angles)) 4
    ;; float64[2] _body_velocity
    (* 8    2)
    ;; float64 _body_height
    8
    ;; float64 _body_width
    8
    ;; float64 _yaw_speed
    8
    ;; float64 _controller_timer
    8
    ;; float64[] _qdd_target
    (* 8    (length _qdd_target)) 4
    ;; float64[] _qdd_actual
    (* 8    (length _qdd_actual)) 4
    ;; float64[] _tool_acc_values
    (* 8    (length _tool_acc_values)) 4
    ;; float64 _robot_mode
    8
    ;; float64 _digital_input_bits
    8
    ;; float64 _test_value
    8
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
     ;; float64[] _coeff_d
     (write-long (length _coeff_d) s)
     (dotimes (i (length _coeff_d))
       (sys::poke (elt _coeff_d i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _coeff_p
     (write-long (length _coeff_p) s)
     (dotimes (i (length _coeff_p))
       (sys::poke (elt _coeff_p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
     ;; float64[] _tcp_speed
     (write-long (length _tcp_speed) s)
     (dotimes (i (length _tcp_speed))
       (sys::poke (elt _tcp_speed i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
     ;; float64[] _body_position
     (write-long (length _body_position) s)
     (dotimes (i (length _body_position))
       (sys::poke (elt _body_position i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _euler_angles
     (write-long (length _euler_angles) s)
     (dotimes (i (length _euler_angles))
       (sys::poke (elt _euler_angles i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[2] _body_velocity
     (dotimes (i 2)
       (sys::poke (elt _body_velocity i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _body_height
       (sys::poke _body_height (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _body_width
       (sys::poke _body_width (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_speed
       (sys::poke _yaw_speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _controller_timer
       (sys::poke _controller_timer (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _qdd_target
     (write-long (length _qdd_target) s)
     (dotimes (i (length _qdd_target))
       (sys::poke (elt _qdd_target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _qdd_actual
     (write-long (length _qdd_actual) s)
     (dotimes (i (length _qdd_actual))
       (sys::poke (elt _qdd_actual i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _tool_acc_values
     (write-long (length _tool_acc_values) s)
     (dotimes (i (length _tool_acc_values))
       (sys::poke (elt _tool_acc_values i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _robot_mode
       (sys::poke _robot_mode (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _digital_input_bits
       (sys::poke _digital_input_bits (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _test_value
       (sys::poke _test_value (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; float64[] _coeff_d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _coeff_d (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _coeff_d i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _coeff_p
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _coeff_p (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _coeff_p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
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
   ;; float64[] _tcp_speed
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tcp_speed (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tcp_speed i) (sys::peek buf ptr- :double)) (incf ptr- 8)
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
   ;; float64[] _body_position
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _body_position (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _body_position i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _euler_angles
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _euler_angles (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _euler_angles i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[2] _body_velocity
   (dotimes (i (length _body_velocity))
     (setf (elt _body_velocity i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64 _body_height
     (setq _body_height (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _body_width
     (setq _body_width (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_speed
     (setq _yaw_speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _controller_timer
     (setq _controller_timer (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _qdd_target
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qdd_target (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _qdd_target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _qdd_actual
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qdd_actual (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _qdd_actual i) (sys::peek buf ptr- :double)) (incf ptr- 8)
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
   ;; float64 _digital_input_bits
     (setq _digital_input_bits (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _test_value
     (setq _test_value (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get arm_msgs::LegState :md5sum-) "a0089be61b27ab5d286d873396fd9097")
(setf (get arm_msgs::LegState :datatype-) "arm_msgs/LegState")
(setf (get arm_msgs::LegState :definition-)
      "Header header
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



(provide :arm_msgs/LegState "a0089be61b27ab5d286d873396fd9097")


