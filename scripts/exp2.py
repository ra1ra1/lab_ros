#!/usr/bin/env python
import sys, rospy
from pimouse_ros.msg import LightSensorValues
from subprocess import call
from subprocess import Popen

with open('fvalue_with_time.csv', 'w') as fwt:
		fwt.write("")

t=0.0
cnt=0 #count
interval=5
f=10
cmd="./plot_time.sh"

if __name__ == '__main__':
    devfile = '/dev/rtlightsensor0'
    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)

    rate = rospy.Rate(f)
    while not rospy.is_shutdown():
	try:
	    with open(devfile, 'r') as df:
		    data = df.readline().split()
		    data = [ int(e) for e in data ]
		    d = LightSensorValues()
		    d.right_forward = data[0]
		    d.right_side = data[1]
		    d.left_side = data[2]
		    d.left_forward = data[3]
		    d.sum_all = sum(data)
		    d.sum_forward = data[0]+data[3]
		    pub.publish(d)
	except IOError:
	    rospy.logerr("cannot write to " + devfile)
	
	with open('fvalue_with_time.csv', 'a') as fwt:
	    fwt.write(str(t)+","+str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+"\n")
	    t+=(1.0/f)
	    cnt+=1
	if (cnt%(f*interval)==0):	
	    plot_time = Popen(cmd, shell=True)

	rate.sleep()
