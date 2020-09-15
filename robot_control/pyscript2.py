from robot_control_class import RobotControl
import time as t

rc = RobotControl()

rc.stop_robot()

#Robot is set up
while True:
  d = rc.get_laser(360)
  #Goes from 360 to check in front of the robot

  #First Condition: Is there a wall in front of the robot

  if ( d < 1.0 ):
      rc.stop_robot()
      # Stop Robot
  else:
      rc.move_straight()
      # Move Forward
  print("dist =", d)


