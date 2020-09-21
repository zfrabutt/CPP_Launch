#! /usr/bin/env python

import rospy
from move_bb8_in_circle_custom.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
import time
from geometry_msgs.msg import Twist

def my_callback(request):
    
    my_response = MyCustomServiceMessageResponse()
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False

    cmd_vel.linear.x = .3
    cmd_vel.angular.z = .3
    pub.publish(cmd_vel)
    time.sleep(request.duration)
    cmd_vel.linear.x = .0
    cmd_vel.angular.z = .0
    pub.publish(cmd_vel)

    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse


cmd_vel = Twist()
cmd_vel.linear.x = 0.0 
cmd_vel.angular.z = 0.0 #want to modify z for turning

rospy.init_node('move_bb8_in_circle')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
rospy.spin()
##rate = rospy.Rate(10)

##while not rospy.is_shutdown(): 
##  pub.publish(cmd_vel)
##  rate.sleep()