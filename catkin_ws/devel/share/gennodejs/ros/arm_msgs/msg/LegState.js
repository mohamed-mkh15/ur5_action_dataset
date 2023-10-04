// Auto-generated. Do not edit!

// (in-package arm_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class LegState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.q_target = null;
      this.coeff_d = null;
      this.coeff_p = null;
      this.qd_target = null;
      this.i_target = null;
      this.tau_target = null;
      this.tool_vector_target = null;
      this.q_actual = null;
      this.qd_actual = null;
      this.i_actual = null;
      this.tau_actual = null;
      this.tcp_force = null;
      this.tool_vector_actual = null;
      this.tcp_speed = null;
      this.motor_temperatures = null;
      this.joint_modes = null;
      this.body_position = null;
      this.euler_angles = null;
      this.body_velocity = null;
      this.body_height = null;
      this.body_width = null;
      this.yaw_speed = null;
      this.controller_timer = null;
      this.qdd_target = null;
      this.qdd_actual = null;
      this.tool_acc_values = null;
      this.robot_mode = null;
      this.digital_input_bits = null;
      this.test_value = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('q_target')) {
        this.q_target = initObj.q_target
      }
      else {
        this.q_target = [];
      }
      if (initObj.hasOwnProperty('coeff_d')) {
        this.coeff_d = initObj.coeff_d
      }
      else {
        this.coeff_d = [];
      }
      if (initObj.hasOwnProperty('coeff_p')) {
        this.coeff_p = initObj.coeff_p
      }
      else {
        this.coeff_p = [];
      }
      if (initObj.hasOwnProperty('qd_target')) {
        this.qd_target = initObj.qd_target
      }
      else {
        this.qd_target = [];
      }
      if (initObj.hasOwnProperty('i_target')) {
        this.i_target = initObj.i_target
      }
      else {
        this.i_target = [];
      }
      if (initObj.hasOwnProperty('tau_target')) {
        this.tau_target = initObj.tau_target
      }
      else {
        this.tau_target = [];
      }
      if (initObj.hasOwnProperty('tool_vector_target')) {
        this.tool_vector_target = initObj.tool_vector_target
      }
      else {
        this.tool_vector_target = [];
      }
      if (initObj.hasOwnProperty('q_actual')) {
        this.q_actual = initObj.q_actual
      }
      else {
        this.q_actual = [];
      }
      if (initObj.hasOwnProperty('qd_actual')) {
        this.qd_actual = initObj.qd_actual
      }
      else {
        this.qd_actual = [];
      }
      if (initObj.hasOwnProperty('i_actual')) {
        this.i_actual = initObj.i_actual
      }
      else {
        this.i_actual = [];
      }
      if (initObj.hasOwnProperty('tau_actual')) {
        this.tau_actual = initObj.tau_actual
      }
      else {
        this.tau_actual = [];
      }
      if (initObj.hasOwnProperty('tcp_force')) {
        this.tcp_force = initObj.tcp_force
      }
      else {
        this.tcp_force = [];
      }
      if (initObj.hasOwnProperty('tool_vector_actual')) {
        this.tool_vector_actual = initObj.tool_vector_actual
      }
      else {
        this.tool_vector_actual = [];
      }
      if (initObj.hasOwnProperty('tcp_speed')) {
        this.tcp_speed = initObj.tcp_speed
      }
      else {
        this.tcp_speed = [];
      }
      if (initObj.hasOwnProperty('motor_temperatures')) {
        this.motor_temperatures = initObj.motor_temperatures
      }
      else {
        this.motor_temperatures = [];
      }
      if (initObj.hasOwnProperty('joint_modes')) {
        this.joint_modes = initObj.joint_modes
      }
      else {
        this.joint_modes = [];
      }
      if (initObj.hasOwnProperty('body_position')) {
        this.body_position = initObj.body_position
      }
      else {
        this.body_position = [];
      }
      if (initObj.hasOwnProperty('euler_angles')) {
        this.euler_angles = initObj.euler_angles
      }
      else {
        this.euler_angles = [];
      }
      if (initObj.hasOwnProperty('body_velocity')) {
        this.body_velocity = initObj.body_velocity
      }
      else {
        this.body_velocity = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('body_height')) {
        this.body_height = initObj.body_height
      }
      else {
        this.body_height = 0.0;
      }
      if (initObj.hasOwnProperty('body_width')) {
        this.body_width = initObj.body_width
      }
      else {
        this.body_width = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_speed')) {
        this.yaw_speed = initObj.yaw_speed
      }
      else {
        this.yaw_speed = 0.0;
      }
      if (initObj.hasOwnProperty('controller_timer')) {
        this.controller_timer = initObj.controller_timer
      }
      else {
        this.controller_timer = 0.0;
      }
      if (initObj.hasOwnProperty('qdd_target')) {
        this.qdd_target = initObj.qdd_target
      }
      else {
        this.qdd_target = [];
      }
      if (initObj.hasOwnProperty('qdd_actual')) {
        this.qdd_actual = initObj.qdd_actual
      }
      else {
        this.qdd_actual = [];
      }
      if (initObj.hasOwnProperty('tool_acc_values')) {
        this.tool_acc_values = initObj.tool_acc_values
      }
      else {
        this.tool_acc_values = [];
      }
      if (initObj.hasOwnProperty('robot_mode')) {
        this.robot_mode = initObj.robot_mode
      }
      else {
        this.robot_mode = 0.0;
      }
      if (initObj.hasOwnProperty('digital_input_bits')) {
        this.digital_input_bits = initObj.digital_input_bits
      }
      else {
        this.digital_input_bits = 0.0;
      }
      if (initObj.hasOwnProperty('test_value')) {
        this.test_value = initObj.test_value
      }
      else {
        this.test_value = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LegState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [q_target]
    bufferOffset = _arraySerializer.float64(obj.q_target, buffer, bufferOffset, null);
    // Serialize message field [coeff_d]
    bufferOffset = _arraySerializer.float64(obj.coeff_d, buffer, bufferOffset, null);
    // Serialize message field [coeff_p]
    bufferOffset = _arraySerializer.float64(obj.coeff_p, buffer, bufferOffset, null);
    // Serialize message field [qd_target]
    bufferOffset = _arraySerializer.float64(obj.qd_target, buffer, bufferOffset, null);
    // Serialize message field [i_target]
    bufferOffset = _arraySerializer.float64(obj.i_target, buffer, bufferOffset, null);
    // Serialize message field [tau_target]
    bufferOffset = _arraySerializer.float64(obj.tau_target, buffer, bufferOffset, null);
    // Serialize message field [tool_vector_target]
    bufferOffset = _arraySerializer.float64(obj.tool_vector_target, buffer, bufferOffset, null);
    // Serialize message field [q_actual]
    bufferOffset = _arraySerializer.float64(obj.q_actual, buffer, bufferOffset, null);
    // Serialize message field [qd_actual]
    bufferOffset = _arraySerializer.float64(obj.qd_actual, buffer, bufferOffset, null);
    // Serialize message field [i_actual]
    bufferOffset = _arraySerializer.float64(obj.i_actual, buffer, bufferOffset, null);
    // Serialize message field [tau_actual]
    bufferOffset = _arraySerializer.float64(obj.tau_actual, buffer, bufferOffset, null);
    // Serialize message field [tcp_force]
    bufferOffset = _arraySerializer.float64(obj.tcp_force, buffer, bufferOffset, null);
    // Serialize message field [tool_vector_actual]
    bufferOffset = _arraySerializer.float64(obj.tool_vector_actual, buffer, bufferOffset, null);
    // Serialize message field [tcp_speed]
    bufferOffset = _arraySerializer.float64(obj.tcp_speed, buffer, bufferOffset, null);
    // Serialize message field [motor_temperatures]
    bufferOffset = _arraySerializer.float64(obj.motor_temperatures, buffer, bufferOffset, null);
    // Serialize message field [joint_modes]
    bufferOffset = _arraySerializer.float64(obj.joint_modes, buffer, bufferOffset, null);
    // Serialize message field [body_position]
    bufferOffset = _arraySerializer.float64(obj.body_position, buffer, bufferOffset, null);
    // Serialize message field [euler_angles]
    bufferOffset = _arraySerializer.float64(obj.euler_angles, buffer, bufferOffset, null);
    // Check that the constant length array field [body_velocity] has the right length
    if (obj.body_velocity.length !== 2) {
      throw new Error('Unable to serialize array field body_velocity - length must be 2')
    }
    // Serialize message field [body_velocity]
    bufferOffset = _arraySerializer.float64(obj.body_velocity, buffer, bufferOffset, 2);
    // Serialize message field [body_height]
    bufferOffset = _serializer.float64(obj.body_height, buffer, bufferOffset);
    // Serialize message field [body_width]
    bufferOffset = _serializer.float64(obj.body_width, buffer, bufferOffset);
    // Serialize message field [yaw_speed]
    bufferOffset = _serializer.float64(obj.yaw_speed, buffer, bufferOffset);
    // Serialize message field [controller_timer]
    bufferOffset = _serializer.float64(obj.controller_timer, buffer, bufferOffset);
    // Serialize message field [qdd_target]
    bufferOffset = _arraySerializer.float64(obj.qdd_target, buffer, bufferOffset, null);
    // Serialize message field [qdd_actual]
    bufferOffset = _arraySerializer.float64(obj.qdd_actual, buffer, bufferOffset, null);
    // Serialize message field [tool_acc_values]
    bufferOffset = _arraySerializer.float64(obj.tool_acc_values, buffer, bufferOffset, null);
    // Serialize message field [robot_mode]
    bufferOffset = _serializer.float64(obj.robot_mode, buffer, bufferOffset);
    // Serialize message field [digital_input_bits]
    bufferOffset = _serializer.float64(obj.digital_input_bits, buffer, bufferOffset);
    // Serialize message field [test_value]
    bufferOffset = _serializer.float64(obj.test_value, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LegState
    let len;
    let data = new LegState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [q_target]
    data.q_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [coeff_d]
    data.coeff_d = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [coeff_p]
    data.coeff_p = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [qd_target]
    data.qd_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [i_target]
    data.i_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tau_target]
    data.tau_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tool_vector_target]
    data.tool_vector_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [q_actual]
    data.q_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [qd_actual]
    data.qd_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [i_actual]
    data.i_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tau_actual]
    data.tau_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tcp_force]
    data.tcp_force = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tool_vector_actual]
    data.tool_vector_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tcp_speed]
    data.tcp_speed = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [motor_temperatures]
    data.motor_temperatures = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [joint_modes]
    data.joint_modes = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [body_position]
    data.body_position = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [euler_angles]
    data.euler_angles = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [body_velocity]
    data.body_velocity = _arrayDeserializer.float64(buffer, bufferOffset, 2)
    // Deserialize message field [body_height]
    data.body_height = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [body_width]
    data.body_width = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_speed]
    data.yaw_speed = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [controller_timer]
    data.controller_timer = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [qdd_target]
    data.qdd_target = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [qdd_actual]
    data.qdd_actual = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tool_acc_values]
    data.tool_acc_values = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [robot_mode]
    data.robot_mode = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [digital_input_bits]
    data.digital_input_bits = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [test_value]
    data.test_value = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.q_target.length;
    length += 8 * object.coeff_d.length;
    length += 8 * object.coeff_p.length;
    length += 8 * object.qd_target.length;
    length += 8 * object.i_target.length;
    length += 8 * object.tau_target.length;
    length += 8 * object.tool_vector_target.length;
    length += 8 * object.q_actual.length;
    length += 8 * object.qd_actual.length;
    length += 8 * object.i_actual.length;
    length += 8 * object.tau_actual.length;
    length += 8 * object.tcp_force.length;
    length += 8 * object.tool_vector_actual.length;
    length += 8 * object.tcp_speed.length;
    length += 8 * object.motor_temperatures.length;
    length += 8 * object.joint_modes.length;
    length += 8 * object.body_position.length;
    length += 8 * object.euler_angles.length;
    length += 8 * object.qdd_target.length;
    length += 8 * object.qdd_actual.length;
    length += 8 * object.tool_acc_values.length;
    return length + 156;
  }

  static datatype() {
    // Returns string type for a message object
    return 'arm_msgs/LegState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a0089be61b27ab5d286d873396fd9097';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LegState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.q_target !== undefined) {
      resolved.q_target = msg.q_target;
    }
    else {
      resolved.q_target = []
    }

    if (msg.coeff_d !== undefined) {
      resolved.coeff_d = msg.coeff_d;
    }
    else {
      resolved.coeff_d = []
    }

    if (msg.coeff_p !== undefined) {
      resolved.coeff_p = msg.coeff_p;
    }
    else {
      resolved.coeff_p = []
    }

    if (msg.qd_target !== undefined) {
      resolved.qd_target = msg.qd_target;
    }
    else {
      resolved.qd_target = []
    }

    if (msg.i_target !== undefined) {
      resolved.i_target = msg.i_target;
    }
    else {
      resolved.i_target = []
    }

    if (msg.tau_target !== undefined) {
      resolved.tau_target = msg.tau_target;
    }
    else {
      resolved.tau_target = []
    }

    if (msg.tool_vector_target !== undefined) {
      resolved.tool_vector_target = msg.tool_vector_target;
    }
    else {
      resolved.tool_vector_target = []
    }

    if (msg.q_actual !== undefined) {
      resolved.q_actual = msg.q_actual;
    }
    else {
      resolved.q_actual = []
    }

    if (msg.qd_actual !== undefined) {
      resolved.qd_actual = msg.qd_actual;
    }
    else {
      resolved.qd_actual = []
    }

    if (msg.i_actual !== undefined) {
      resolved.i_actual = msg.i_actual;
    }
    else {
      resolved.i_actual = []
    }

    if (msg.tau_actual !== undefined) {
      resolved.tau_actual = msg.tau_actual;
    }
    else {
      resolved.tau_actual = []
    }

    if (msg.tcp_force !== undefined) {
      resolved.tcp_force = msg.tcp_force;
    }
    else {
      resolved.tcp_force = []
    }

    if (msg.tool_vector_actual !== undefined) {
      resolved.tool_vector_actual = msg.tool_vector_actual;
    }
    else {
      resolved.tool_vector_actual = []
    }

    if (msg.tcp_speed !== undefined) {
      resolved.tcp_speed = msg.tcp_speed;
    }
    else {
      resolved.tcp_speed = []
    }

    if (msg.motor_temperatures !== undefined) {
      resolved.motor_temperatures = msg.motor_temperatures;
    }
    else {
      resolved.motor_temperatures = []
    }

    if (msg.joint_modes !== undefined) {
      resolved.joint_modes = msg.joint_modes;
    }
    else {
      resolved.joint_modes = []
    }

    if (msg.body_position !== undefined) {
      resolved.body_position = msg.body_position;
    }
    else {
      resolved.body_position = []
    }

    if (msg.euler_angles !== undefined) {
      resolved.euler_angles = msg.euler_angles;
    }
    else {
      resolved.euler_angles = []
    }

    if (msg.body_velocity !== undefined) {
      resolved.body_velocity = msg.body_velocity;
    }
    else {
      resolved.body_velocity = new Array(2).fill(0)
    }

    if (msg.body_height !== undefined) {
      resolved.body_height = msg.body_height;
    }
    else {
      resolved.body_height = 0.0
    }

    if (msg.body_width !== undefined) {
      resolved.body_width = msg.body_width;
    }
    else {
      resolved.body_width = 0.0
    }

    if (msg.yaw_speed !== undefined) {
      resolved.yaw_speed = msg.yaw_speed;
    }
    else {
      resolved.yaw_speed = 0.0
    }

    if (msg.controller_timer !== undefined) {
      resolved.controller_timer = msg.controller_timer;
    }
    else {
      resolved.controller_timer = 0.0
    }

    if (msg.qdd_target !== undefined) {
      resolved.qdd_target = msg.qdd_target;
    }
    else {
      resolved.qdd_target = []
    }

    if (msg.qdd_actual !== undefined) {
      resolved.qdd_actual = msg.qdd_actual;
    }
    else {
      resolved.qdd_actual = []
    }

    if (msg.tool_acc_values !== undefined) {
      resolved.tool_acc_values = msg.tool_acc_values;
    }
    else {
      resolved.tool_acc_values = []
    }

    if (msg.robot_mode !== undefined) {
      resolved.robot_mode = msg.robot_mode;
    }
    else {
      resolved.robot_mode = 0.0
    }

    if (msg.digital_input_bits !== undefined) {
      resolved.digital_input_bits = msg.digital_input_bits;
    }
    else {
      resolved.digital_input_bits = 0.0
    }

    if (msg.test_value !== undefined) {
      resolved.test_value = msg.test_value;
    }
    else {
      resolved.test_value = 0.0
    }

    return resolved;
    }
};

module.exports = LegState;
