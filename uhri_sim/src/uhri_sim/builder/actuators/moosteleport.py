from morse.builder.creator import ActuatorCreator

class Moosteleport(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "uhri_sim.actuators.moosteleport.Moosteleport",\
                                 "moosteleport")

