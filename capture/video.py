import os, sys, time
import numpy as np
import cv2

VIDEO_WIDTH = 416
VIDEO_HEIGHT = 416
VIDEO_FOLDER = '/Users/frank/Development/shoptrail/shoptrail-camera/videos/'

def returnCap(id):
    try:
        cap = cv2.VideoCapture(id)
        cap.release()
        cap = cv2.VideoCapture(id)
        return cap
    except:
        print("could not open camera capture object")

def getVideoInfo(VIDEO_FOLDER):
    try:
        cap = returnCap(VIDEO_FOLDER)
        if cap.isOpened():
            width = cap.get(3)
            height = cap.get(4)
            fps = cap.get(cv2.CAP_PROP_FPS)

            cap.release()
            return (width, height, fps)
    except:
        cap.release()
        print("Unexpected error:", sys.exc_info()[0])
        raise


def resizeVideo(inp, dest="", target_width=VIDEO_WIDTH, target_height=VIDEO_HEIGHT):
    import moviepy.editor as mp
    clip = mp.VideoFileClip(input)
    clip_resized = clip.resize(width=target_width, height=target_height)
    path_parts = os.path.splitext(inp)
    dest = dest if dest else path_parts[0] + '_resized' + path_parts[1]
    clip_resized.write_videofile(dest)
    return dest

def captureVideoFromFile(fileName, save, default_size=False):
    source = VIDEO_FOLDER + fileName
    if default_size:
        (width, height, fps) = getVideoInfo(source)
        size = (width, height)
        displayVideo(source, "file", size)
    else:
        displayVideo(source, "file")


def captureVideoFromCamera(cameraId, save):
    source = cameraId
    displayVideo(cameraId, "camera")

def displayVideo(source, type="camera", size=(VIDEO_WIDTH, VIDEO_HEIGHT)):
    print("source is {}".format(source))
    print("frame size is:{}".format(size))

    cap = returnCap(source)
    width = cap.set(3, VIDEO_WIDTH)
    height = cap.set(4, VIDEO_HEIGHT)
    # cap.set(cv2.CAP_PROP_EXPOSURE, 40)

    ## fix: remove late
    timeout = time.time() + 10
    ## fix: remove later

    while(cap.isOpened()):
        # Capture frame-by-frame
        if time.time() > timeout:
            break;
        ret, frame = cap.read()

        if(type =="file"):
            frame = cv2.resize(frame, size, interpolation = cv2.INTER_LINEAR);

        if ret:
        # Our operations on the frame come here
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', frame)
        # pause for defined period in millisecons; if passed '0' it waits for any or defined (key) event
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

    # When finished release the capture
    cap.release()
    cv2.destroyAllWindows()
