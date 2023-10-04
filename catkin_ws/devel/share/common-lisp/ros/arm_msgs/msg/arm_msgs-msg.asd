
(cl:in-package :asdf)

(defsystem "arm_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GripperState" :depends-on ("_package_GripperState"))
    (:file "_package_GripperState" :depends-on ("_package"))
    (:file "LegState" :depends-on ("_package_LegState"))
    (:file "_package_LegState" :depends-on ("_package"))
    (:file "ManipulatorState" :depends-on ("_package_ManipulatorState"))
    (:file "_package_ManipulatorState" :depends-on ("_package"))
  ))