#!/usr/bin/env python
from pydarknet import Detector, Image
import numpy as np
from constants import *


class YoloV3Model():

    def get_model():

        net = Detector(
                bytes("cfg/yolov3-tiny.cfg", encoding="utf-8"),
                bytes("weights/yolov2-tiny.weights", encoding="utf-8"), 0,
                bytes("cfg/coco.data", encoding="utf-8")
        )
    return net
        # net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
