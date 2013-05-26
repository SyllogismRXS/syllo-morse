#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <videoray_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from videoray_sim.builder.robots import Videoray


human = Human()

# 'morse add robot <name> videoray_sim' can help you to build custom robots.
#robot = Morsy()
robot = Videoray()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot.translate(1.0, 0.0, 0.0)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> videoray_sim' can help you with the creation of a custom
# actuator.
motion = MotionVW()
robot.append(motion)


# Add a keyboard controller to move the robot with arrow keys.
keyboard = Keyboard()
robot.append(keyboard)

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> videoray_sim' can help you with the creation of a custom
# sensor.
pose = Pose()
robot.append(pose)

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html 
# the other available interfaces (like ROS, YARP...)
robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
#env = Environment('sandbox', fastmode = False)
env = Environment('water-1/water_scene', fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

