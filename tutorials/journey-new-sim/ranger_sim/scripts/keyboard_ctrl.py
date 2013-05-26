from pymorse import Morse

def pose_received(pose):
    print("The Ranger is currently at %s" % pose)


print("Use WASD to control the Ranger")

with Morse() as simu:
    #simu.robot.pose.subscribe(pose_received)

    motion = simu.robot.motion
    eyes = simu.robot.eyes

    v = 0.0
    w = 0.0

    left = 0.0
    right = 0.0

    while True:
        #key = input("WASD?")
        key = input("WASD (eyes:RFTG)?")

        if key.lower() == "w":
            v += 0.1
        elif key.lower() == "s":
            v -= 0.1
        elif key.lower() == "a":
            w += 0.1
        elif key.lower() == "d":
            w -= 0.1

        elif key.lower() == "r":
            left += 0.1
        elif key.lower() == "f":
            left -= 0.1
        elif key.lower() == "t":
            right += 0.1
        elif key.lower() == "g":
            right -= 0.1

        else:
            continue

        motion.publish({"v": v, "w": w})
        eyes.publish({"left": left, "right": right})
