from morse.builder import *

class Turtlebot(Robot):
    """
    A template robot model for turtlebot, with a motion controller and a pose sensor.
    """
    def __init__(self, debug = True):

        # turtlebot.blend is located in the data/robots directory
        Robot.__init__(self, 'turtlebot_sim/robots/turtlebot.blend')
        self.properties(classpath = "turtlebot_sim.robots.turtlebot.Turtlebot")

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

