import cv2

from video import VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_PATH

def saveImage(image, label):
    file_count = "_%03d" % count
    cv2.imwrite(VIDEO_PATH + label + "_" + file_count + ".jpg", image)

def video2images(video_path, label, target_width=VIDEO_WIDTH, target_height=VIDEO_HEIGHT):
    cap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    print("process started successfully")
    count = 0
    while success:
        resize = cv2.resize(image, (target_width, target_height), interpolation = cv2.INTER_LINEAR)
        file_count = "_%03d" % count
        cv2.imwrite(VIDEO_PATH + label + "_" + file_count + ".jpg", resize)
        if cv2.waitKey(10) == 27:
            break
        count += 1
