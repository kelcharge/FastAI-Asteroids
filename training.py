from fastai.vision.all import *
import time
import cv2
from utils.grabscreen import grab_screen
from datetime import datetime
import os

def label_func(x): return x.parent.name

model = "x-model"

def run():
    path = Path("images")
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")

    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=40, num_workers=0)

    if os.path.isfile(model + ".pth"):
        learn = vision_learner(dls, resnet18, metrics=accuracy).load(model)
    else:
        learn = vision_learner(dls, resnet18, metrics=accuracy)

    early_stop = EarlyStoppingCallback(monitor='accuracy', min_delta=0.01, patience=5)
    #learn = vision_learner(dls, resnet34, metrics=accuracy, pretrained=False)
    #learn = Learner(dls, xresnet34(n_out=4), metrics=accuracy)
    print("Loaded")
    #learn.lr_find()
    learn.fine_tune(15, base_lr=1.0e-02, cbs=[SaveModelCallback(fname=datetime.now().strftime("%Y%m%d%H%M%S") + "-model"), early_stop])
    #learn.fit_one_cycle(4, 1e-3, cbs=[SaveModelCallback(fname='net')])

    learn.export(datetime.now().strftime("%Y%m%d%H%M%S") + '.pkl')


if __name__ == '__main__':
    run()