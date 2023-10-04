// Auto-generated. Do not edit!

// (in-package robotiq_2f_gripper_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Robotiq2FGripper_robot_input {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.gACT = null;
      this.gGTO = null;
      this.gSTA = null;
      this.gOBJ = null;
      this.gFLT = null;
      this.gPR = null;
      this.gPO = null;
      this.gCU = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('gACT')) {
        this.gACT = initObj.gACT
      }
      else {
        this.gACT = 0;
      }
      if (initObj.hasOwnProperty('gGTO')) {
        this.gGTO = initObj.gGTO
      }
      else {
        this.gGTO = 0;
      }
      if (initObj.hasOwnProperty('gSTA')) {
        this.gSTA = initObj.gSTA
      }
      else {
        this.gSTA = 0;
      }
      if (initObj.hasOwnProperty('gOBJ')) {
        this.gOBJ = initObj.gOBJ
      }
      else {
        this.gOBJ = 0;
      }
      if (initObj.hasOwnProperty('gFLT')) {
        this.gFLT = initObj.gFLT
      }
      else {
        this.gFLT = 0;
      }
      if (initObj.hasOwnProperty('gPR')) {
        this.gPR = initObj.gPR
      }
      else {
        this.gPR = 0;
      }
      if (initObj.hasOwnProperty('gPO')) {
        this.gPO = initObj.gPO
      }
      else {
        this.gPO = 0;
      }
      if (initObj.hasOwnProperty('gCU')) {
        this.gCU = initObj.gCU
      }
      else {
        this.gCU = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Robotiq2FGripper_robot_input
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [gACT]
    bufferOffset = _serializer.uint8(obj.gACT, buffer, bufferOffset);
    // Serialize message field [gGTO]
    bufferOffset = _serializer.uint8(obj.gGTO, buffer, bufferOffset);
    // Serialize message field [gSTA]
    bufferOffset = _serializer.uint8(obj.gSTA, buffer, bufferOffset);
    // Serialize message field [gOBJ]
    bufferOffset = _serializer.uint8(obj.gOBJ, buffer, bufferOffset);
    // Serialize message field [gFLT]
    bufferOffset = _serializer.uint8(obj.gFLT, buffer, bufferOffset);
    // Serialize message field [gPR]
    bufferOffset = _serializer.uint8(obj.gPR, buffer, bufferOffset);
    // Serialize message field [gPO]
    bufferOffset = _serializer.uint8(obj.gPO, buffer, bufferOffset);
    // Serialize message field [gCU]
    bufferOffset = _serializer.uint8(obj.gCU, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Robotiq2FGripper_robot_input
    let len;
    let data = new Robotiq2FGripper_robot_input(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [gACT]
    data.gACT = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gGTO]
    data.gGTO = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gSTA]
    data.gSTA = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gOBJ]
    data.gOBJ = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gFLT]
    data.gFLT = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gPR]
    data.gPR = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gPO]
    data.gPO = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gCU]
    data.gCU = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robotiq_2f_gripper_control/Robotiq2FGripper_robot_input';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '482d848f6e07a7c5352784b8f561a8ea';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint8 gACT 
    uint8 gGTO 
    uint8 gSTA 
    uint8 gOBJ 
    uint8 gFLT
    uint8 gPR
    uint8 gPO
    uint8 gCU
    
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
    const resolved = new Robotiq2FGripper_robot_input(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.gACT !== undefined) {
      resolved.gACT = msg.gACT;
    }
    else {
      resolved.gACT = 0
    }

    if (msg.gGTO !== undefined) {
      resolved.gGTO = msg.gGTO;
    }
    else {
      resolved.gGTO = 0
    }

    if (msg.gSTA !== undefined) {
      resolved.gSTA = msg.gSTA;
    }
    else {
      resolved.gSTA = 0
    }

    if (msg.gOBJ !== undefined) {
      resolved.gOBJ = msg.gOBJ;
    }
    else {
      resolved.gOBJ = 0
    }

    if (msg.gFLT !== undefined) {
      resolved.gFLT = msg.gFLT;
    }
    else {
      resolved.gFLT = 0
    }

    if (msg.gPR !== undefined) {
      resolved.gPR = msg.gPR;
    }
    else {
      resolved.gPR = 0
    }

    if (msg.gPO !== undefined) {
      resolved.gPO = msg.gPO;
    }
    else {
      resolved.gPO = 0
    }

    if (msg.gCU !== undefined) {
      resolved.gCU = msg.gCU;
    }
    else {
      resolved.gCU = 0
    }

    return resolved;
    }
};

module.exports = Robotiq2FGripper_robot_input;
