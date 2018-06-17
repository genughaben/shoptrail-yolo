import numpy as np
import cv2

IMAGES_FOLDER = "/Users/frank/Development/shoptrail/shoptrail-camera/images/"

# Load an color image in grayscale
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread(IMAGES_FOLDER + 'kollegen.jpg', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(IMAGES_FOLDER + 'messigray.png',img)
    cv2.destroyAllWindows()
