#! /usr/bin/env python
#! /usr/bin/env python

import rospy
import rospkg
# Import the service message used by the service /trajectory_by_name
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
execute_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
execute_trajectory_request_object = ExecTrajRequest()

rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

execute_trajectory_request_object.file = traj
# Create an object of type TrajByNameRequest
#traj_by_name_object = TrajByNameRequest()
# Fill the variable traj_name of this object with the desired value
#traj_by_name_object.traj_name = "release_food"
#traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
# Send through the connection the name of the trajectory to be executed by the robot
result = execute_trajectory_service(execute_trajectory_request_object)
# Print the result given by the service called
print result