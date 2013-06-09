import logging; logger = logging.getLogger("morse.builder." + __name__)
import math
from morse.builder.creator import SensorCreator, bpymorse
from morse.builder.blenderobjects import *

class Completestate(SensorCreator):
    def __init__(self, name=None):
        SensorCreator.__init__(self, name, "videoray_sim.sensors.completestate.Completestate", "completestate")
        mesh = Cube("CompletestateCube")
        mesh.scale = (.04, .04, .02)
        mesh.color(.3, .9, .6)
        self.append(mesh)
