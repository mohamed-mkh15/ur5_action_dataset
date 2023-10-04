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

class GripperState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.coeff_p = null;
      this.gripper_cmd = null;
      this.gripper_status = null;
      this.ee_ft = null;
      this.gripper_joints = null;
      this.gripper_torque = null;
      this.coeff_d = null;
      this.gripper_speed = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('coeff_p')) {
        this.coeff_p = initObj.coeff_p
      }
      else {
        this.coeff_p = [];
      }
      if (initObj.hasOwnProperty('gripper_cmd')) {
        this.gripper_cmd = initObj.gripper_cmd
      }
      else {
        this.gripper_cmd = [];
      }
      if (initObj.hasOwnProperty('gripper_status')) {
        this.gripper_status = initObj.gripper_status
      }
      else {
        this.gripper_status = [];
      }
      if (initObj.hasOwnProperty('ee_ft')) {
        this.ee_ft = initObj.ee_ft
      }
      else {
        this.ee_ft = [];
      }
      if (initObj.hasOwnProperty('gripper_joints')) {
        this.gripper_joints = initObj.gripper_joints
      }
      else {
        this.gripper_joints = [];
      }
      if (initObj.hasOwnProperty('gripper_torque')) {
        this.gripper_torque = initObj.gripper_torque
      }
      else {
        this.gripper_torque = 0.0;
      }
      if (initObj.hasOwnProperty('coeff_d')) {
        this.coeff_d = initObj.coeff_d
      }
      else {
        this.coeff_d = [];
      }
      if (initObj.hasOwnProperty('gripper_speed')) {
        this.gripper_speed = initObj.gripper_speed
      }
      else {
        this.gripper_speed = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GripperState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [coeff_p]
    bufferOffset = _arraySerializer.float64(obj.coeff_p, buffer, bufferOffset, null);
    // Serialize message field [gripper_cmd]
    bufferOffset = _arraySerializer.uint8(obj.gripper_cmd, buffer, bufferOffset, null);
    // Serialize message field [gripper_status]
    bufferOffset = _arraySerializer.uint8(obj.gripper_status, buffer, bufferOffset, null);
    // Serialize message field [ee_ft]
    bufferOffset = _arraySerializer.float32(obj.ee_ft, buffer, bufferOffset, null);
    // Serialize message field [gripper_joints]
    bufferOffset = _arraySerializer.float64(obj.gripper_joints, buffer, bufferOffset, null);
    // Serialize message field [gripper_torque]
    bufferOffset = _serializer.float64(obj.gripper_torque, buffer, bufferOffset);
    // Serialize message field [coeff_d]
    bufferOffset = _arraySerializer.float64(obj.coeff_d, buffer, bufferOffset, null);
    // Serialize message field [gripper_speed]
    bufferOffset = _arraySerializer.float64(obj.gripper_speed, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GripperState
    let len;
    let data = new GripperState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [coeff_p]
    data.coeff_p = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [gripper_cmd]
    data.gripper_cmd = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    // Deserialize message field [gripper_status]
    data.gripper_status = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    // Deserialize message field [ee_ft]
    data.ee_ft = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [gripper_joints]
    data.gripper_joints = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [gripper_torque]
    data.gripper_torque = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [coeff_d]
    data.coeff_d = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [gripper_speed]
    data.gripper_speed = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.coeff_p.length;
    length += object.gripper_cmd.length;
    length += object.gripper_status.length;
    length += 4 * object.ee_ft.length;
    length += 8 * object.gripper_joints.length;
    length += 8 * object.coeff_d.length;
    length += 8 * object.gripper_speed.length;
    return length + 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'arm_msgs/GripperState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '11c92e29e7ae9eb5b85345e361142462';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GripperState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.coeff_p !== undefined) {
      resolved.coeff_p = msg.coeff_p;
    }
    else {
      resolved.coeff_p = []
    }

    if (msg.gripper_cmd !== undefined) {
      resolved.gripper_cmd = msg.gripper_cmd;
    }
    else {
      resolved.gripper_cmd = []
    }

    if (msg.gripper_status !== undefined) {
      resolved.gripper_status = msg.gripper_status;
    }
    else {
      resolved.gripper_status = []
    }

    if (msg.ee_ft !== undefined) {
      resolved.ee_ft = msg.ee_ft;
    }
    else {
      resolved.ee_ft = []
    }

    if (msg.gripper_joints !== undefined) {
      resolved.gripper_joints = msg.gripper_joints;
    }
    else {
      resolved.gripper_joints = []
    }

    if (msg.gripper_torque !== undefined) {
      resolved.gripper_torque = msg.gripper_torque;
    }
    else {
      resolved.gripper_torque = 0.0
    }

    if (msg.coeff_d !== undefined) {
      resolved.coeff_d = msg.coeff_d;
    }
    else {
      resolved.coeff_d = []
    }

    if (msg.gripper_speed !== undefined) {
      resolved.gripper_speed = msg.gripper_speed;
    }
    else {
      resolved.gripper_speed = []
    }

    return resolved;
    }
};

module.exports = GripperState;
