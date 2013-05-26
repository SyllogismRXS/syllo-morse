from morse.builder.creator import ActuatorCreator

class Eyes(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "ranger_sim.actuators.eyes.Eyes",\
                                 "eyes")

