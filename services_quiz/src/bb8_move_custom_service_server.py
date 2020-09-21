#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes 
                                                                                         # generated from MyCustomServiceMessage.srv.

def my_callback(request):
    
    my_response = BB8CustomServiceMessageResponse()
    my_response.success = True
    length = request.side
    print("help")

    for i in range (0, request.repetitions):
        for j in range (0, 4):
            cmd_vel.linear.x = 0.5
            #pub.publish(cmd_vel)
            time.sleep(length)

            cmd_vel.linear.x = 0.0
            #pub.publish(cmd_vel)
            time.sleep(length)

            cmd_vel.angular.z = 0.5
            #pub.publish(cmd_vel)
            time.sleep(1.45)

            cmd_vel.angular.z = 0.0
            #pub.publish(cmd_vel)
            time.sleep(1.45)


    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

cmd_vel = Twist()
cmd_vel.linear.x = 0.0 #want to modify x for speed
cmd_vel.angular.z = 0.0 #want to modify z for turning
rospy.init_node('service_server') 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
#rospy.spin() # maintain the service open.

rate = rospy.Rate(10)


while not rospy.is_shutdown(): 
  pub.publish(cmd_vel)
  rate.sleep()