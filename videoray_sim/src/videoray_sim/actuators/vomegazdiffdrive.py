import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

class Vomegazdiffdrive(morse.core.actuator.Actuator):
    _name = "Vomegazdiffdrive"
    _short_desc = "Controls ROV movement"

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description
    add_data('v', 0.0, 'float',
             'linear velocity in x direction (forward movement) (m/s)')
    add_data('w', 0.0, 'float', 'angular velocity (rad/s)')

    add_data('depth_vel', 0.0, 'float', 'linear velocity in y direction')

    add_property('_type', 'Position', 'ControlType', 'string',
                 "Kind of control, can be one of ['Velocity', 'Position']")


    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)

        # Do here actuator specific initializations

        #self._target_count = 0 # dummy internal variable, for testing purposes

        logger.info('Component initialized')


    @service
    def set_speed(self, v, w, depth_vel):
        """
        Modifies v and w according to the parameters
        
        :param v: desired linear velocity (meter by second)
        :param w: desired angular velocity (radian by second)
        :param depth_vel: desired linear velocity in z-direction (meter by second)
        """
        self.local_data['v'] = v
        self.local_data['w'] = w
        self.local_data['depth_vel'] = depth_vel

    @service
    def stop(self):
        """
        Stop the robot

        Internally, it sets (v, w, depth_vel) to (0.0, 0.0, 0.0)
        """
        self.local_data['v'] = 0.0
        self.local_data['w'] = 0.0
        self.local_data['depth_vel'] = 0.0

    def default_action(self):
        """ Apply (v, w, z) to the parent robot. """

        # Reset movement variables
        vx, vy, vz = 0.0, 0.0, 0.0
        rx, ry, rz = 0.0, 0.0, 0.0
        
        # Scale the speeds to the time used by Blender
        try:
            if self._type == 'Position':
                vx = self.local_data['v'] / self.frequency
                vz = self.local_data['depth_vel'] / self.frequency
                rz = self.local_data['w'] / self.frequency
            elif self._type == 'Velocity':
                vx = self.local_data['v']
                vz = self.local_data['depth_vel']
                rz = self.local_data['w']
        # For the moment ignoring the division by zero
        # It happens apparently when the simulation starts
        except ZeroDivisionError:
            pass

        self.apply_speed(self._type, [vx, vy, vz], [rx, ry, rz])

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
    #
    #def default_action(self):
    #    """ Main loop of the actuator.
    #
    #    Implements the component behaviour
    #    """
    #
    #    # check if we have an on-going asynchronous tasks...
    #    if self._target_count and self.local_data['counter'] > self._target_count:
    #        self.completed(status.SUCCESS, self.local_data['counter'])
    #
    #    # implement here the behaviour of your actuator
    #    self.local_data['counter'] += 1
