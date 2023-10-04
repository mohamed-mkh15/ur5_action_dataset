; Auto-generated. Do not edit!


(cl:in-package robotiq_2f_gripper_control-msg)


;//! \htmlinclude Robotiq2FGripper_robot_input.msg.html

(cl:defclass <Robotiq2FGripper_robot_input> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (gACT
    :reader gACT
    :initarg :gACT
    :type cl:fixnum
    :initform 0)
   (gGTO
    :reader gGTO
    :initarg :gGTO
    :type cl:fixnum
    :initform 0)
   (gSTA
    :reader gSTA
    :initarg :gSTA
    :type cl:fixnum
    :initform 0)
   (gOBJ
    :reader gOBJ
    :initarg :gOBJ
    :type cl:fixnum
    :initform 0)
   (gFLT
    :reader gFLT
    :initarg :gFLT
    :type cl:fixnum
    :initform 0)
   (gPR
    :reader gPR
    :initarg :gPR
    :type cl:fixnum
    :initform 0)
   (gPO
    :reader gPO
    :initarg :gPO
    :type cl:fixnum
    :initform 0)
   (gCU
    :reader gCU
    :initarg :gCU
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Robotiq2FGripper_robot_input (<Robotiq2FGripper_robot_input>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Robotiq2FGripper_robot_input>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Robotiq2FGripper_robot_input)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robotiq_2f_gripper_control-msg:<Robotiq2FGripper_robot_input> is deprecated: use robotiq_2f_gripper_control-msg:Robotiq2FGripper_robot_input instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:header-val is deprecated.  Use robotiq_2f_gripper_control-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'gACT-val :lambda-list '(m))
(cl:defmethod gACT-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gACT-val is deprecated.  Use robotiq_2f_gripper_control-msg:gACT instead.")
  (gACT m))

(cl:ensure-generic-function 'gGTO-val :lambda-list '(m))
(cl:defmethod gGTO-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gGTO-val is deprecated.  Use robotiq_2f_gripper_control-msg:gGTO instead.")
  (gGTO m))

(cl:ensure-generic-function 'gSTA-val :lambda-list '(m))
(cl:defmethod gSTA-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gSTA-val is deprecated.  Use robotiq_2f_gripper_control-msg:gSTA instead.")
  (gSTA m))

(cl:ensure-generic-function 'gOBJ-val :lambda-list '(m))
(cl:defmethod gOBJ-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gOBJ-val is deprecated.  Use robotiq_2f_gripper_control-msg:gOBJ instead.")
  (gOBJ m))

(cl:ensure-generic-function 'gFLT-val :lambda-list '(m))
(cl:defmethod gFLT-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gFLT-val is deprecated.  Use robotiq_2f_gripper_control-msg:gFLT instead.")
  (gFLT m))

(cl:ensure-generic-function 'gPR-val :lambda-list '(m))
(cl:defmethod gPR-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gPR-val is deprecated.  Use robotiq_2f_gripper_control-msg:gPR instead.")
  (gPR m))

(cl:ensure-generic-function 'gPO-val :lambda-list '(m))
(cl:defmethod gPO-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gPO-val is deprecated.  Use robotiq_2f_gripper_control-msg:gPO instead.")
  (gPO m))

(cl:ensure-generic-function 'gCU-val :lambda-list '(m))
(cl:defmethod gCU-val ((m <Robotiq2FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_2f_gripper_control-msg:gCU-val is deprecated.  Use robotiq_2f_gripper_control-msg:gCU instead.")
  (gCU m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Robotiq2FGripper_robot_input>) ostream)
  "Serializes a message object of type '<Robotiq2FGripper_robot_input>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gACT)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGTO)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gOBJ)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFLT)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPR)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPO)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCU)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Robotiq2FGripper_robot_input>) istream)
  "Deserializes a message object of type '<Robotiq2FGripper_robot_input>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gACT)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGTO)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gOBJ)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFLT)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPR)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPO)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCU)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Robotiq2FGripper_robot_input>)))
  "Returns string type for a message object of type '<Robotiq2FGripper_robot_input>"
  "robotiq_2f_gripper_control/Robotiq2FGripper_robot_input")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Robotiq2FGripper_robot_input)))
  "Returns string type for a message object of type 'Robotiq2FGripper_robot_input"
  "robotiq_2f_gripper_control/Robotiq2FGripper_robot_input")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Robotiq2FGripper_robot_input>)))
  "Returns md5sum for a message object of type '<Robotiq2FGripper_robot_input>"
  "482d848f6e07a7c5352784b8f561a8ea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Robotiq2FGripper_robot_input)))
  "Returns md5sum for a message object of type 'Robotiq2FGripper_robot_input"
  "482d848f6e07a7c5352784b8f561a8ea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Robotiq2FGripper_robot_input>)))
  "Returns full string definition for message of type '<Robotiq2FGripper_robot_input>"
  (cl:format cl:nil "Header header~%uint8 gACT ~%uint8 gGTO ~%uint8 gSTA ~%uint8 gOBJ ~%uint8 gFLT~%uint8 gPR~%uint8 gPO~%uint8 gCU~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Robotiq2FGripper_robot_input)))
  "Returns full string definition for message of type 'Robotiq2FGripper_robot_input"
  (cl:format cl:nil "Header header~%uint8 gACT ~%uint8 gGTO ~%uint8 gSTA ~%uint8 gOBJ ~%uint8 gFLT~%uint8 gPR~%uint8 gPO~%uint8 gCU~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Robotiq2FGripper_robot_input>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Robotiq2FGripper_robot_input>))
  "Converts a ROS message object to a list"
  (cl:list 'Robotiq2FGripper_robot_input
    (cl:cons ':header (header msg))
    (cl:cons ':gACT (gACT msg))
    (cl:cons ':gGTO (gGTO msg))
    (cl:cons ':gSTA (gSTA msg))
    (cl:cons ':gOBJ (gOBJ msg))
    (cl:cons ':gFLT (gFLT msg))
    (cl:cons ':gPR (gPR msg))
    (cl:cons ':gPO (gPO msg))
    (cl:cons ':gCU (gCU msg))
))
