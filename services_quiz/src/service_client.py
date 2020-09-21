#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
print("help 1")
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/move_bb8_in_square_custom')
# Create the connection to the service
print("help 2")

BB8_custom_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
# Create an object of type TrajByNameRequest
BB8_custom_object = BB8CustomServiceMessageRequest()
# Fill the variable traj_name of this object with the desired value
BB8_custom_object.side = 3
BB8_custom_object.repetitions = 2
# Send through the connection the name of the trajectory to be executed by the robot
result = BB8_custom_service(BB8_custom_object)

BB8_custom_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
# Create an object of type TrajByNameRequest
BB8_custom_object = BB8CustomServiceMessageRequest()
# Fill the variable traj_name of this object with the desired value
BB8_custom_object.side = 4
BB8_custom_object.repetitions = 1
# Send through the connection the name of the trajectory to be executed by the robot
result = BB8_custom_service(BB8_custom_object)
# Print the result given by the service called
print result