
"use strict";

let GetSafetyMode = require('./GetSafetyMode.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let Popup = require('./Popup.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let AddToLog = require('./AddToLog.js')
let GetRobotMode = require('./GetRobotMode.js')
let Load = require('./Load.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let GetProgramState = require('./GetProgramState.js')
let RawRequest = require('./RawRequest.js')

module.exports = {
  GetSafetyMode: GetSafetyMode,
  IsProgramSaved: IsProgramSaved,
  Popup: Popup,
  IsProgramRunning: IsProgramRunning,
  IsInRemoteControl: IsInRemoteControl,
  AddToLog: AddToLog,
  GetRobotMode: GetRobotMode,
  Load: Load,
  GetLoadedProgram: GetLoadedProgram,
  GetProgramState: GetProgramState,
  RawRequest: RawRequest,
};
