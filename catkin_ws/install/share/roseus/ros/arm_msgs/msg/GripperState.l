;; Auto-generated. Do not edit!


(when (boundp 'arm_msgs::GripperState)
  (if (not (find-package "ARM_MSGS"))
    (make-package "ARM_MSGS"))
  (shadow 'GripperState (find-package "ARM_MSGS")))
(unless (find-package "ARM_MSGS::GRIPPERSTATE")
  (make-package "ARM_MSGS::GRIPPERSTATE"))

(in-package "ROS")
;;//! \htmlinclude GripperState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass arm_msgs::GripperState
  :super ros::object
  :slots (_header _coeff_p _gripper_cmd _gripper_status _ee_ft _gripper_joints _gripper_torque _coeff_d _gripper_speed ))

(defmethod arm_msgs::GripperState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:coeff_p __coeff_p) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:gripper_cmd __gripper_cmd) (make-array 0 :initial-element 0 :element-type :char))
    ((:gripper_status __gripper_status) (make-array 0 :initial-element 0 :element-type :char))
    ((:ee_ft __ee_ft) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:gripper_joints __gripper_joints) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:gripper_torque __gripper_torque) 0.0)
    ((:coeff_d __coeff_d) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:gripper_speed __gripper_speed) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _coeff_p __coeff_p)
   (setq _gripper_cmd __gripper_cmd)
   (setq _gripper_status __gripper_status)
   (setq _ee_ft __ee_ft)
   (setq _gripper_joints __gripper_joints)
   (setq _gripper_torque (float __gripper_torque))
   (setq _coeff_d __coeff_d)
   (setq _gripper_speed __gripper_speed)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:coeff_p
   (&optional __coeff_p)
   (if __coeff_p (setq _coeff_p __coeff_p)) _coeff_p)
  (:gripper_cmd
   (&optional __gripper_cmd)
   (if __gripper_cmd (setq _gripper_cmd __gripper_cmd)) _gripper_cmd)
  (:gripper_status
   (&optional __gripper_status)
   (if __gripper_status (setq _gripper_status __gripper_status)) _gripper_status)
  (:ee_ft
   (&optional __ee_ft)
   (if __ee_ft (setq _ee_ft __ee_ft)) _ee_ft)
  (:gripper_joints
   (&optional __gripper_joints)
   (if __gripper_joints (setq _gripper_joints __gripper_joints)) _gripper_joints)
  (:gripper_torque
   (&optional __gripper_torque)
   (if __gripper_torque (setq _gripper_torque __gripper_torque)) _gripper_torque)
  (:coeff_d
   (&optional __coeff_d)
   (if __coeff_d (setq _coeff_d __coeff_d)) _coeff_d)
  (:gripper_speed
   (&optional __gripper_speed)
   (if __gripper_speed (setq _gripper_speed __gripper_speed)) _gripper_speed)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64[] _coeff_p
    (* 8    (length _coeff_p)) 4
    ;; uint8[] _gripper_cmd
    (* 1    (length _gripper_cmd)) 4
    ;; uint8[] _gripper_status
    (* 1    (length _gripper_status)) 4
    ;; float32[] _ee_ft
    (* 4    (length _ee_ft)) 4
    ;; float64[] _gripper_joints
    (* 8    (length _gripper_joints)) 4
    ;; float64 _gripper_torque
    8
    ;; float64[] _coeff_d
    (* 8    (length _coeff_d)) 4
    ;; float64[] _gripper_speed
    (* 8    (length _gripper_speed)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64[] _coeff_p
     (write-long (length _coeff_p) s)
     (dotimes (i (length _coeff_p))
       (sys::poke (elt _coeff_p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; uint8[] _gripper_cmd
     (write-long (length _gripper_cmd) s)
     (princ _gripper_cmd s)
     ;; uint8[] _gripper_status
     (write-long (length _gripper_status) s)
     (princ _gripper_status s)
     ;; float32[] _ee_ft
     (write-long (length _ee_ft) s)
     (dotimes (i (length _ee_ft))
       (sys::poke (elt _ee_ft i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float64[] _gripper_joints
     (write-long (length _gripper_joints) s)
     (dotimes (i (length _gripper_joints))
       (sys::poke (elt _gripper_joints i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _gripper_torque
       (sys::poke _gripper_torque (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _coeff_d
     (write-long (length _coeff_d) s)
     (dotimes (i (length _coeff_d))
       (sys::poke (elt _coeff_d i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _gripper_speed
     (write-long (length _gripper_speed) s)
     (dotimes (i (length _gripper_speed))
       (sys::poke (elt _gripper_speed i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64[] _coeff_p
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _coeff_p (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _coeff_p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; uint8[] _gripper_cmd
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _gripper_cmd (make-array n :element-type :char))
     (replace _gripper_cmd buf :start2 ptr-) (incf ptr- n))
   ;; uint8[] _gripper_status
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _gripper_status (make-array n :element-type :char))
     (replace _gripper_status buf :start2 ptr-) (incf ptr- n))
   ;; float32[] _ee_ft
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _ee_ft (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _ee_ft i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float64[] _gripper_joints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _gripper_joints (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _gripper_joints i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _gripper_torque
     (setq _gripper_torque (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _coeff_d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _coeff_d (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _coeff_d i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _gripper_speed
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _gripper_speed (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _gripper_speed i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get arm_msgs::GripperState :md5sum-) "11c92e29e7ae9eb5b85345e361142462")
(setf (get arm_msgs::GripperState :datatype-) "arm_msgs/GripperState")
(setf (get arm_msgs::GripperState :definition-)
      "Header header
float64[] coeff_p # a floating-point number representing a proporsional coefficient for feedback loop
uint8[] gripper_cmd # sequence of bits which representing the command to the gripper
uint8[] gripper_status # sequence of bits which representing the status of the gripper
float32[] ee_ft # 3 forces and 3 torques on the end-effector with additinal sensor
float64[] gripper_joints # a floating-point number representing an angle of gripper
float64 gripper_torque # a floating-point number representing a torque value on gripper joint
float64[] coeff_d # a floating-point number representing a differential coefficient for feedback loop
float64[] gripper_speed # a floating-point number representing velocity of the gripper joints.
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



(provide :arm_msgs/GripperState "11c92e29e7ae9eb5b85345e361142462")


