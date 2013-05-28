from morse.builder.creator import ActuatorCreator

class Vomegazdiffdrive(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "videoray_sim.actuators.vomegazdiffdrive.Vomegazdiffdrive",\
                                 "vomegazdiffdrive")

