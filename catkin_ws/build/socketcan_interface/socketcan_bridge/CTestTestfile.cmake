# CMake generated Testfile for 
# Source directory: /home/mkh15/catkin_ws/src/socketcan_interface/socketcan_bridge
# Build directory: /home/mkh15/catkin_ws/build/socketcan_interface/socketcan_bridge
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_socketcan_bridge_gtest_test_conversion "/home/mkh15/catkin_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/mkh15/catkin_ws/build/test_results/socketcan_bridge/gtest-test_conversion.xml" "--return-code" "/home/mkh15/catkin_ws/devel/lib/socketcan_bridge/test_conversion --gtest_output=xml:/home/mkh15/catkin_ws/build/test_results/socketcan_bridge/gtest-test_conversion.xml")
add_test(_ctest_socketcan_bridge_rostest_test_to_socketcan.test "/home/mkh15/catkin_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/mkh15/catkin_ws/build/test_results/socketcan_bridge/rostest-test_to_socketcan.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/mkh15/catkin_ws/src/socketcan_interface/socketcan_bridge --package=socketcan_bridge --results-filename test_to_socketcan.xml --results-base-dir \"/home/mkh15/catkin_ws/build/test_results\" /home/mkh15/catkin_ws/src/socketcan_interface/socketcan_bridge/test/to_socketcan.test ")
add_test(_ctest_socketcan_bridge_rostest_test_to_topic.test "/home/mkh15/catkin_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/mkh15/catkin_ws/build/test_results/socketcan_bridge/rostest-test_to_topic.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/mkh15/catkin_ws/src/socketcan_interface/socketcan_bridge --package=socketcan_bridge --results-filename test_to_topic.xml --results-base-dir \"/home/mkh15/catkin_ws/build/test_results\" /home/mkh15/catkin_ws/src/socketcan_interface/socketcan_bridge/test/to_topic.test ")
