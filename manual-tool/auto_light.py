# PIP:
# python3 -m pip install busylight-for-humans
# python3 -m pip install opencv-python


# Prepare busylight
from busylight.lights.embrava import Blynclight
light = Blynclight.first_light()

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_yellow = (255, 255, 0)


# Prepare OpenCV
import cv2

def checkAllOpenedCams():
    # checks the first 10 indexes.
    cameras, availables = [], []
    for i in range(0, 10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cameras.append(i)
        else:
            # Cannot open
            cap.release()
            continue
        try:
            ret, frame = cap.read()
            if not ret:
                continue
        except Exception as e:
            print('camera already used')
            cap.release()
            continue
        availables.append(i)
        cap.release()
    return cameras, availables

def releaseCam():
    # When everything done, release the capture
    print("Releasing...")
    cv2.destroyAllWindows()
    print("Released")


# Prepare exit handling
import signal
import time
def handler(signum, frame):
    releaseCam()
    exit(1)

signal.signal(signal.SIGINT, handler)

# Get looping
import sched, time
s = sched.scheduler(time.time, time.sleep)
def run(sc): 
    cameras, availables = checkAllOpenedCams()
    if len(cameras) == len(availables):
        light.on(color_green)
    elif len(cameras) > len(availables):
        light.on(color_red)
    else:
        print("Error:", cameras, availables)
    sc.enter(5, 1, run, (sc,))

s.enter(1, 1, run, (s,))
s.run()

releaseCam()