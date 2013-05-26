from morse.builder import *

atrv = ATRV()

motion = MotionVW()
motion.translate(z=0.3)
atrv.append(motion)

pose = Pose()
pose.translate(z=0.83)
atrv.append(pose)

#pose.add_stream('socket')
#pose.configure_service('socket')
#motion.configure_service('socket')

#pose.add_stream('ros')
#motion.add_stream('ros')
atrv.add_default_interface('ros')

env = Environment('indoors-1/indoor-1')
env.place_camera([5,-5,6])
env.aim_camera([1.0470, 0, 0.7854])
