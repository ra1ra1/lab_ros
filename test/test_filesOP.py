#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

class filesOPTest(unittest.TestCase):
    def test_node_exit(self):
	nodes = rosnode.get_node_names()
	self.assertIn('/filesOP', nodes, "node does not exit")

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('test_filesOP')
    rostest.rosrun('lab_ros', 'test_filesOP', filesOPTest)
