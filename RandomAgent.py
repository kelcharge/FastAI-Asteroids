import random
import time

from utils.getkeys import key_check
import pydirectinput
from pynput.keyboard import Key, Controller
import keyboard
from utils.directkeys import PressKey, ReleaseKey, LEFT, RIGHT

keyboard2 = Controller()

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Randomly pick action then sleep.
# 0 do nothing release everything
# 1 hold left
# 2 hold right
# 3 Press Shoot

while True:
    action = random.randint(0,3)

    if action == 0:
        keyboard2.release(Key.left)
        keyboard2.release(Key.right)
        keyboard2.release(Key.space)
        time.sleep(sleepy)

    if action == 1:
        keyboard2.release(Key.right)
        keyboard2.release(Key.space)
        keyboard2.press(Key.left)
        time.sleep(sleepy)

    if action == 2:
        keyboard2.release(Key.left)
        keyboard2.release(Key.space)
        keyboard2.press(Key.right)
        time.sleep(sleepy)

    if action == 3:
        keyboard2.release(Key.left)
        keyboard2.release(Key.right)
        keyboard2.press(Key.space)
        time.sleep(sleepy)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break