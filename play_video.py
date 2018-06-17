import optparse
from capture.video import captureVideoFromFile, captureVideoFromCamera

import string, random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option(
        "-c", type="int", dest="cameraId", default = 0,
        help = "Specify Camera to capture from (optional)"
    )

    parser.add_option(
        "-f", type="string", dest="fileName", default = "",
        help = "File for playback (optional)"
    )

    parser.add_option(
        "-s", action="store_true", dest="save", default=False,
        help = "save images to disk (optionals)"
    )

    random_label = id_generator(4)
    parser.add_option(
        "-l", dest="label", default=random_label,
        help = "Label indicating image class (optional)"
    )

    (options, args) = parser.parse_args()
    print(options)

    if(options.cameraId):
        captureVideoFromCamera(options.cameraId, options.save)
    elif(options.fileName):
        captureVideoFromFile(options.fileName, options.save)
