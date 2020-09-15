from robot_control_class import RobotControl
#Used to import RobotControl Class
import time as t

rc = RobotControl()

a = rc.get_laser(360)

print ("The distance measured is: ", a)

i = 225

while True:
    d = rc.get_laser_full()
    print(type(d))
    print("i = ", i, " d= ", d)
    i = i + 1
    if (i > 719):
        i = 0
    t.sleep(0.1)