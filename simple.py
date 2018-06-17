import time
import numpy as np
import cv2

VIDEO_WIDTH = 416
VIDEO_HEIGHT = 416

cap = cv2.VideoCapture(0)

width = cap.set(3, VIDEO_WIDTH)
height = cap.set(4, VIDEO_HEIGHT)

timeout = time.time() + 10
while(True):
    if time.time() > timeout:
        break;
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
