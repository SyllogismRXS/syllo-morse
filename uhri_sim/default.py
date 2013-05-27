#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <uhri_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from videoray_sim.builder.robots import Videoray
from diver_sim.builder.robots import Diver

#
# VideoRay Configuration
#
robot = Videoray()
robot.translate(0.0, 0.0, 2)

motion = MotionVW()
robot.append(motion)

keyboard = Keyboard()
robot.append(keyboard)

pose = Pose()
robot.append(pose)

robot.add_default_interface('socket')

#
# Diver Configuration
#
diver = Diver()
diver.translate(1.0, 1.0, 2)

#motion = MotionVW()
#robot.append(motion)

#keyboard = Keyboard()
#robot.append(keyboard)

diver_pose = Pose()
diver.append(diver_pose)

diver.add_default_interface('socket')

#
# Environment Setup
#
# set 'fastmode' to True to switch to wireframe mode
env = Environment('water-1/water_scene', fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

