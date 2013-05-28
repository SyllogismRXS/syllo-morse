from morse.builder import *

class Videoray(Robot):
    """
    A template robot model for videoray, with a motion controller and a pose sensor.
    """
    def __init__(self, debug = True):

        # videoray.blend is located in the data/robots directory
        Robot.__init__(self, 'videoray_sim/robots/videoray.blend')
        self.properties(classpath = "videoray_sim.robots.videoray.Videoray")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        #self.motion = MotionVW()
        #self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        #if debug:
            #keyboard = Keyboard()
            #self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

