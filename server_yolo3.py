#!/usr/bin/env python
import time
from flask import Flask, render_template, Response
import cv2
from pydarknet import Detector, Image
import numpy as np
from constants import *

app = Flask(__name__)
cap = cv2.VideoCapture(0)
width = cap.set(3, VIDEO_WIDTH*2)
height = cap.set(4, VIDEO_HEIGHT*3)
print("video_dimensions - width: {}, height: {}".format(width,height))

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

def get_model():
    global net

    net = Detector(bytes("cfg/yolov3-tiny.cfg", encoding="utf-8"), bytes("weights/yolov2-tiny.weights", encoding="utf-8"), 0,
                   bytes("cfg/coco.data", encoding="utf-8"))
    # net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                   # bytes("cfg/coco.data", encoding="utf-8"))

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""

    get_model()

    while True:
        ret, frame = cap.read()
        if ret:
            # time.sleep(0.5)

            start_time = time.time()
            # here comes yolo into play
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            dark_frame = Image(frame)
            results = net.detect(dark_frame)
            del dark_frame

            end_time = time.time()
            print("Elapsed Time:",end_time-start_time)

            print("prediction: {}".format(results))
            for cat, score, bounds in results:
                print(results)
                if score > 0.5:
                    x, y, w, h = bounds
                    cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
                    cv2.putText(frame,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

            cv2.imwrite('t.jpg', frame)
            # print('FPS {:.1f}'.format(1 / (time.time() - stime)))
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')



@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
