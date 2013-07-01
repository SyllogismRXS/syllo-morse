from morse.builder import *

class Diver(Robot):
    """
    A template robot model for diver, with a motion controller and a pose sensor.
    """
    def __init__(self, debug = True):

        # diver.blend is located in the data/robots directory
        Robot.__init__(self, 'diver_sim/robots/diver.blend')
        self.properties(classpath = "diver_sim.robots.diver.Diver")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

