#! /usr/bin/env morseexec

from morse.builder import *

human = Human()

#b21 = B21()
#jido = Jido()

pioneer3dx = Pioneer3DX()
pioneer3dx.translate(3,3,3)

sub = Submarine()
sub.translate(3,3,3)

#hummer = Hummer()
#hummer.translate(3,3,3)

#quad = Quadrotor()
#quad.translate(3,3,3)

#vic = Victim()


# Import the pose sensor and attach it to the human.
pose = Pose()
human.append(pose)

# Import, configure and place a static object from 'kitchen_objects.blend'.
cornflakes = PassiveObject("props/kitchen_objects", "Cornflakes")
cornflakes.setgraspable()
cornflakes.properties(Label = "My cornflakes")
cornflakes.translate(-7, 3, 1.1)

human.add_default_interface('ros')

#env = Environment('indoors-1/indoor-1')
#env = Environment('laas/grande_salle')
#env = Environment('water-1/deep_water')
#env = Environment('water-1/water_scene')
#env = Environment('human_tut/tutorial_scene')
#env = Environment('indoors-1/boxes')

#human.translate(3,5,0) # need to translate, otherwise, human falls
#env = Environment('tum_kitchen/tum_kitchen')
#env = Environment('land-1/buildings_1')
#human.translate(5,5,5) # need to translate, otherwise, human is in building
#env = Environment('land-1/buildings_2')
#env = Environment('land-1/rosace_1')
env = Environment('land-1/trees')


