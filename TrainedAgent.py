import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
from pynput.keyboard import Key, Controller
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, LEFT, RIGHT
from fastai.vision.all import *

keyboard2 = Controller()

def label_func(x): return x.parent.name
print("Enter filename: ")
filename = input()
learn_inf = load_learner("E:/workspace/python/" + filename + ".pkl")
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

while True:

    image = grab_screen(region=(10, 50, 810, 590))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(224,224))

    #cv2.imshow("AI Peak", image)
    #cv2.waitKey(1)

    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]

    
    if action == "Shoot" or result[2][0]>.1:
        #print(f"SHOOT! - {result[1]}")
        keyboard2.release(Key.left)
        keyboard2.release(Key.right)
        keyboard2.press(Key.space)
        time.sleep(sleepy)

    # if action == "Nothing" or result[2][1]>.1:
    #     #print(f"Nothing! - {result[1]}")
    #     keyboard2.release(Key.left)
    #     keyboard2.release(Key.right)
    #     keyboard2.release(Key.space)
    #     time.sleep(sleepy)

    if action == "Left":
        #print(f"LEFT! - {result[1]}")
        keyboard2.release(Key.right)
        keyboard2.release(Key.space)
        keyboard2.press(Key.left)
        time.sleep(sleepy)

    if action == "Right":
        #print(f"Right! - {result[1]}")
        keyboard2.release(Key.left)
        keyboard2.release(Key.space)
        keyboard2.press(Key.right)
        time.sleep(sleepy)


    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break