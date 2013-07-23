#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <uhri_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from diver_sim.builder.robots import Diver
from videoray_sim.builder.robots import Videoray
from videoray_sim.builder.actuators import Vomegazdiffdrive
from videoray_sim.builder.sensors import Completestate

#
# VideoRay Configuration
#
videoray = Videoray()
videoray.translate(0.0, 0.0, 2)

motion = Teleport()
videoray.append(motion)

videoray.add_default_interface('ros')

#
# Diver Configuration
#
diver = Diver()
diver.translate(1.0, 1.0, 2)

motion = Teleport()
diver.append(motion)

diver.add_default_interface('ros')

#
# Environment Setup
#
# set 'fastmode' to True to switch to wireframe mode
env = Environment('water-1/water_scene', fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

