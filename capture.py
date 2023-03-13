import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check


file_name = "data/training_data.npy"
file_name2 = "data/target_data.npy"


def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    print(keys)
    if keys == "B":
        print("Starting")
        break


while True:
    keys = key_check()
    last_time = time.time()

    if keys == "Left" or keys == "Right" or keys == " ":  # only save the images for which we care
        image = grab_screen(region=(10, 50, 810, 590))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (224, 224))

        # Debug line to show image
        # cv2.imshow("AI Peak", image)
        # cv2.waitKey(1)

        # Convert to numpy array
        image = np.array(image)
        image_data.append(image)

        targets.append(keys)

    if keys == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)
