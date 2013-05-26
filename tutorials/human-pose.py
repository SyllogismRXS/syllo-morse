import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist

motion = Twist()
def callback(msg):
    position = msg.pose.position
    print("position: \n" + repr(position))
    
rospy.init_node("hri")
rospy.Subscriber("/human/pose", PoseStamped, callback)
rospy.spin() # this will block untill you hit Ctrl+C
