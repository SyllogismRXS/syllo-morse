import logging; logger = logging.getLogger("morse." + __name__)
from morse.core import blenderapi
from morse.robots.grasper import RobotGrasper
from morse.core.services import service

class Diver(RobotGrasper):
    """ Class definition for the diver as a robot entity
        Sub class of Morse_Object. """

    def __init__(self, obj, parent=None):
        """ Constructor method.
            Receives the reference to the Blender object.
            Optionally it gets the name of the object's parent,
            but that information is not currently used for a robot. """
        # Call the constructor of the parent class
        logger.info('%s initialization' % obj.name)
        RobotGrasper.__init__(self, obj, parent)

        """
        We define here the name of the pr2 grasping hand:
        """
        self.hand_name = 'Hand_Grab.R'


        logger.info('Component initialized')

    @service
    def move(self, speed, rotation):
        """ Move the diver.
        """
        
        diver = self.bge_object
        
        if not diver['Manipulate']:
            diver.applyMovement( [speed,0,0], True )
            diver.applyRotation( [0,0,rotation], True )
        else :
            scene = blenderapi.scene()
            target = scene.objects['IK_Target_Empty.R']

            target.applyMovement([0.0, rotation, 0.0], True)
            target.applyMovement([0.0, 0.0, -speed], True)
        
        
    @service
    def move_head(self, pan, tilt):
        """ Move the diver head.
        """
        
        diver = self.bge_object
        scene = blenderapi.scene()
        target = scene.objects['Target_Empty']
        
        if diver['Manipulate']:
            return

        target.applyMovement([0.0, pan, 0.0], True)
        target.applyMovement([0.0, 0.0, tilt], True)
        
    @service
    def move_hand(self, diff, tilt):
        """ move the diver hand (wheel). a request to use by a socket.
        Done for wiimote remote control.
        """
        
        diver = self.bge_object
        if diver['Manipulate']:
            scene = blenderapi.scene()
            target = scene.objects['IK_Target_Empty.R']
            target.applyMovement([diff, 0.0, 0.0], True)  
        
    @service
    def toggle_manipulation(self):
        """ change from and to manipulation mode. a request to use by a socket.
        Done for wiimote remote control.
        """
        
        diver = self.bge_object
        scene = blenderapi.scene()
        hand_target = scene.objects['IK_Target_Empty.R']
        head_target = scene.objects['Target_Empty']

        if diver['Manipulate']:
            diver['Manipulate'] = False
            # Place the hand beside the body
            hand_target.localPosition = [0.0, -0.3, 0.8]
            head_target.setParent(diver)
            head_target.localPosition = [1.3, 0.0, 1.7]
        else:
            diver['Manipulate'] = True
            head_target.setParent(hand_target)
            # Place the hand in a nice position
            hand_target.localPosition = [0.6, 0.0, 1.4]
            # Place the head in the same place
            head_target.localPosition = [0.0, 0.0, 0.0]
        
    def default_action(self):
        """ Main function of this component. """
        pass
