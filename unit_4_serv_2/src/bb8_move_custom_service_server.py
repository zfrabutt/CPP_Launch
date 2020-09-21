#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from std_srvs.srv import Empty, EmptyResponse
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/my_service')
# Create the connection to the service
empty_service = rospy.ServiceProxy('/my_service', Empty)
# Create an object of type TrajByNameRequest
#traj_by_name_object = TrajByNameRequest
# Fill the variable traj_name of this object with the desired value
#traj_by_name_object.traj_name = "release_food"
# Send through the connection the name of the trajectory to be executed by the robot
result = empty_service()
# Print the result given by the service called
print result