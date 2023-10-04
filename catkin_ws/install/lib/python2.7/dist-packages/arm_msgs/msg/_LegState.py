# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from arm_msgs/LegState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class LegState(genpy.Message):
  _md5sum = "a0089be61b27ab5d286d873396fd9097"
  _type = "arm_msgs/LegState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
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
"""
  __slots__ = ['header','q_target','coeff_d','coeff_p','qd_target','i_target','tau_target','tool_vector_target','q_actual','qd_actual','i_actual','tau_actual','tcp_force','tool_vector_actual','tcp_speed','motor_temperatures','joint_modes','body_position','euler_angles','body_velocity','body_height','body_width','yaw_speed','controller_timer','qdd_target','qdd_actual','tool_acc_values','robot_mode','digital_input_bits','test_value']
  _slot_types = ['std_msgs/Header','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[2]','float64','float64','float64','float64','float64[]','float64[]','float64[]','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,q_target,coeff_d,coeff_p,qd_target,i_target,tau_target,tool_vector_target,q_actual,qd_actual,i_actual,tau_actual,tcp_force,tool_vector_actual,tcp_speed,motor_temperatures,joint_modes,body_position,euler_angles,body_velocity,body_height,body_width,yaw_speed,controller_timer,qdd_target,qdd_actual,tool_acc_values,robot_mode,digital_input_bits,test_value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LegState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.q_target is None:
        self.q_target = []
      if self.coeff_d is None:
        self.coeff_d = []
      if self.coeff_p is None:
        self.coeff_p = []
      if self.qd_target is None:
        self.qd_target = []
      if self.i_target is None:
        self.i_target = []
      if self.tau_target is None:
        self.tau_target = []
      if self.tool_vector_target is None:
        self.tool_vector_target = []
      if self.q_actual is None:
        self.q_actual = []
      if self.qd_actual is None:
        self.qd_actual = []
      if self.i_actual is None:
        self.i_actual = []
      if self.tau_actual is None:
        self.tau_actual = []
      if self.tcp_force is None:
        self.tcp_force = []
      if self.tool_vector_actual is None:
        self.tool_vector_actual = []
      if self.tcp_speed is None:
        self.tcp_speed = []
      if self.motor_temperatures is None:
        self.motor_temperatures = []
      if self.joint_modes is None:
        self.joint_modes = []
      if self.body_position is None:
        self.body_position = []
      if self.euler_angles is None:
        self.euler_angles = []
      if self.body_velocity is None:
        self.body_velocity = [0.] * 2
      if self.body_height is None:
        self.body_height = 0.
      if self.body_width is None:
        self.body_width = 0.
      if self.yaw_speed is None:
        self.yaw_speed = 0.
      if self.controller_timer is None:
        self.controller_timer = 0.
      if self.qdd_target is None:
        self.qdd_target = []
      if self.qdd_actual is None:
        self.qdd_actual = []
      if self.tool_acc_values is None:
        self.tool_acc_values = []
      if self.robot_mode is None:
        self.robot_mode = 0.
      if self.digital_input_bits is None:
        self.digital_input_bits = 0.
      if self.test_value is None:
        self.test_value = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.q_target = []
      self.coeff_d = []
      self.coeff_p = []
      self.qd_target = []
      self.i_target = []
      self.tau_target = []
      self.tool_vector_target = []
      self.q_actual = []
      self.qd_actual = []
      self.i_actual = []
      self.tau_actual = []
      self.tcp_force = []
      self.tool_vector_actual = []
      self.tcp_speed = []
      self.motor_temperatures = []
      self.joint_modes = []
      self.body_position = []
      self.euler_angles = []
      self.body_velocity = [0.] * 2
      self.body_height = 0.
      self.body_width = 0.
      self.yaw_speed = 0.
      self.controller_timer = 0.
      self.qdd_target = []
      self.qdd_actual = []
      self.tool_acc_values = []
      self.robot_mode = 0.
      self.digital_input_bits = 0.
      self.test_value = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.q_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_target))
      length = len(self.coeff_d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.coeff_d))
      length = len(self.coeff_p)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.coeff_p))
      length = len(self.qd_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_target))
      length = len(self.i_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.i_target))
      length = len(self.tau_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tau_target))
      length = len(self.tool_vector_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool_vector_target))
      length = len(self.q_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_actual))
      length = len(self.qd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_actual))
      length = len(self.i_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.i_actual))
      length = len(self.tau_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tau_actual))
      length = len(self.tcp_force)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tcp_force))
      length = len(self.tool_vector_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool_vector_actual))
      length = len(self.tcp_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tcp_speed))
      length = len(self.motor_temperatures)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.motor_temperatures))
      length = len(self.joint_modes)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.joint_modes))
      length = len(self.body_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.body_position))
      length = len(self.euler_angles)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.euler_angles))
      buff.write(_get_struct_2d().pack(*self.body_velocity))
      _x = self
      buff.write(_get_struct_4d().pack(_x.body_height, _x.body_width, _x.yaw_speed, _x.controller_timer))
      length = len(self.qdd_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qdd_target))
      length = len(self.qdd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qdd_actual))
      length = len(self.tool_acc_values)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool_acc_values))
      _x = self
      buff.write(_get_struct_3d().pack(_x.robot_mode, _x.digital_input_bits, _x.test_value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coeff_d = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coeff_p = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.i_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tau_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_vector_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.i_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tau_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_force = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_vector_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_speed = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.motor_temperatures = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_modes = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.body_position = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.euler_angles = s.unpack(str[start:end])
      start = end
      end += 16
      self.body_velocity = _get_struct_2d().unpack(str[start:end])
      _x = self
      start = end
      end += 32
      (_x.body_height, _x.body_width, _x.yaw_speed, _x.controller_timer,) = _get_struct_4d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qdd_target = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qdd_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_acc_values = s.unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.robot_mode, _x.digital_input_bits, _x.test_value,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.q_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_target.tostring())
      length = len(self.coeff_d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.coeff_d.tostring())
      length = len(self.coeff_p)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.coeff_p.tostring())
      length = len(self.qd_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_target.tostring())
      length = len(self.i_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.i_target.tostring())
      length = len(self.tau_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tau_target.tostring())
      length = len(self.tool_vector_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool_vector_target.tostring())
      length = len(self.q_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_actual.tostring())
      length = len(self.qd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_actual.tostring())
      length = len(self.i_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.i_actual.tostring())
      length = len(self.tau_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tau_actual.tostring())
      length = len(self.tcp_force)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tcp_force.tostring())
      length = len(self.tool_vector_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool_vector_actual.tostring())
      length = len(self.tcp_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tcp_speed.tostring())
      length = len(self.motor_temperatures)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.motor_temperatures.tostring())
      length = len(self.joint_modes)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.joint_modes.tostring())
      length = len(self.body_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.body_position.tostring())
      length = len(self.euler_angles)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.euler_angles.tostring())
      buff.write(self.body_velocity.tostring())
      _x = self
      buff.write(_get_struct_4d().pack(_x.body_height, _x.body_width, _x.yaw_speed, _x.controller_timer))
      length = len(self.qdd_target)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qdd_target.tostring())
      length = len(self.qdd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qdd_actual.tostring())
      length = len(self.tool_acc_values)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool_acc_values.tostring())
      _x = self
      buff.write(_get_struct_3d().pack(_x.robot_mode, _x.digital_input_bits, _x.test_value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coeff_d = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coeff_p = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.i_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tau_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_vector_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.i_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tau_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_force = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_vector_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_speed = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.motor_temperatures = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_modes = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.body_position = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.euler_angles = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 16
      self.body_velocity = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=2)
      _x = self
      start = end
      end += 32
      (_x.body_height, _x.body_width, _x.yaw_speed, _x.controller_timer,) = _get_struct_4d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qdd_target = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qdd_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_acc_values = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 24
      (_x.robot_mode, _x.digital_input_bits, _x.test_value,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
