#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg): 
  angles = msg.ranges
  forward = angles[360]
  right = angles[0]
  left = angles[719]

  if (forward > 1):
    cmd_vel.linear.x = .3
  else:
    cmd_vel.linear.x = 0

    if (left > right):
        cmd_vel.angular.z = -.25
        time.sleep(.1)
        cmd_vel.angular.z = 0
    else:
        cmd_vel.angular.z = .25
        time.sleep(.1)
        cmd_vel.angular.z = 0


angles = []
forward = 0.0
right = 0.0
left = 0.0
cmd_vel = Twist()
cmd_vel.linear.x = 0.3 #want to modify x for speed
cmd_vel.angular.z = 0.0 #want to modify z for turning

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.init_node('topics_quiz_node')
rate = rospy.Rate(10)


while not rospy.is_shutdown(): 
  pub.publish(cmd_vel)
  rate.sleep()
  
