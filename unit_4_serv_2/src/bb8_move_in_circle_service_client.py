#! /usr/bin/env python

import rospy
from move_bb8_in_circle_custom.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse  # you import the service message python classes generated from Empty.srv.
import time
from geometry_msgs.msg import Twist

def my_callback(request):
    print "My_callback has been called"

    cmd_vel.linear.x = 0.3 #want to modify x for speed
    cmd_vel.angular.z = 0.3 #want to modify z for turning
    time.sleep(1)

    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 


cmd_vel = Twist()
cmd_vel.linear.x = 0.0 #want to modify x for speed
cmd_vel.angular.z = 0.0 #want to modify z for turning

rospy.init_node('move_bb8_in_circle')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
rate = rospy.Rate(10)

while not rospy.is_shutdown(): 
  pub.publish(cmd_vel)
  rate.sleep()