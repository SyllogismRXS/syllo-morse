import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property
from morse.core import mathutils

class Eyes(morse.core.actuator.Actuator):
    _name = "Eyes"
    _short_desc = "Controls the eyes of the EPFL Ranger Robot"

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description
    add_data('left', 0.1, 'float', 'Left eye rotation, in radians')
    add_data('right', -0.1, 'float', 'Right eye rotation, in radians')
    #add_data('counter', 0, 'int', 'A dummy counter, for testing purposes')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)
        
        # Do here actuator specific initializations
        self.left_eye = parent.bge_object.children["left_eye"]
        self.right_eye = parent.bge_object.children["right_eye"]

        #self._target_count = 0 # dummy internal variable, for testing purposes

        logger.info('Component initialized')

    #@service
    #def get_counter(self):
    #    """ This is a sample service.
    #
    #    Simply returns the value of the internal counter.
    #
    #    You can access it as a RPC service from clients.
    #    """
    #    logger.info("%s counter is %s" % (self.name, self.local_data['counter']))
    #
    #    return self.local_data['counter']
    #
    #@interruptible
    #@async_service
    #def async_test(self, value):
    #    """ This is a sample asynchronous service.
    #
    #    Returns when the internal counter reaches ``value``.
    #
    #    You can access it as a RPC service from clients.
    #    """
    #    self._target_count = value

    def default_action(self):
        """ Main loop of the actuator.

        Implements the component behaviour
        """

        l_orientation = mathutils.Euler([self.local_data['left'], 1.57, 0.0], "ZYX")
        self.left_eye.orientation = l_orientation.to_matrix()

        r_orientation = mathutils.Euler([self.local_data['right'], 1.57, 0.0], "ZYX")
        self.right_eye.orientation = r_orientation.to_matrix()

        # check if we have an on-going asynchronous tasks...
        #if self._target_count and self.local_data['counter'] > self._target_count:
        #    self.completed(status.SUCCESS, self.local_data['counter'])

        # implement here the behaviour of your actuator
        #self.local_data['counter'] += 1
