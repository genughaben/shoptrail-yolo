#!/usr/bin/env python
import time
from flask import Flask, render_template, Response
import cv2
# from darkflow.net.build import TFNet
import numpy as np
from constants import *

app = Flask(__name__)
cap = cv2.VideoCapture(1)
width = cap.set(3, VIDEO_WIDTH)
height = cap.set(4, VIDEO_HEIGHT)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

def get_model():
    option = {
        'model': 'cfg/yolov3.cfg',
        'load': 'weights/yolov3.weights',
        'threshold': 0.15
    }
    tfnet = TFNet(option)
    return tfnet


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    while True:
        ret, frame = cap.read()
        time.sleep(0.2)
        # here comes yolo into play
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # results = tfnet.return_predict(frame)
        # for color, result in zip(colors, results):
        #     tl = (result['topleft']['x'], result['topleft']['y'])
        #     br = (result['bottomright']['x'], result['bottomright']['y'])
        #     label = result['label']
        #     frame = cv2.rectangle(frame, tl, br, color, 7)
        #     frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

        # test graphics
        cv2.line(frame,(0,0),(100,100),(255,0,0),5)
        cv2.rectangle(frame,(50,50),(300,300),(255,0,0),3)
        cv2.circle(frame,(400,200), 63, (0,0,255), -1)

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
    app.run(host='0.0.0.0', debug=True, threaded=True)
