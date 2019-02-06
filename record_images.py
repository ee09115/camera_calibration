import cv2
import argparse

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-rw", "--width", required=False, default="640", help="camera resolution width in pixels")
    ap.add_argument("-rh", "--height", required=False, default="480", help="camera resolution height in pixels")
    ap.add_argument("-fps", "--frame_rate", required=False, default="30", help="camera frame rate (fps)")
    ap.add_argument("-d", "--camera_device", required=True, help="camera device id")
    ap.add_argument("-p", "--path", required=True, help="folder to store images")
    ap.add_argument("-a", "--auto_mode", required=False, default="True", \
                    help="automatic mode grabs a frame ")
    ap.add_argument("-n", "--total_number_of_images", required=True, help="total number of images to capture")
    args = vars(ap.parse_args())

    width = int(args["width"])
    height = int(args["height"])
    framesPerSecond = int(args["frame_rate"])
    numberOfImages = int(args["total_number_of_images"])
    pathToImagesFolder = args["path"]
    deviceID = int(args["camera_device"])
    auto_mode = eval(args["auto_mode"])

    cap = cv2.VideoCapture(deviceID)
    if not cap.isOpened():
        print "Error openning camera:", deviceID
        exit(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, framesPerSecond)

    framesPerSecond = cap.get(cv2.CAP_PROP_FPS)

    it_secs_max = 3
    it = 0
    it_secs = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if auto_mode:
            frameCopy = frame.copy()

            if it % framesPerSecond == 0:
                it_secs += 1
            cv2.putText(frameCopy, str(it_secs), (width // 2, height // 2), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 200), \
                        thickness=2)

            if it_secs > it_secs_max:
                if not cv2.imwrite(pathToImagesFolder + "%d" % numberOfImages + ".jpg", frame):
                    print("Error written images to:", pathToImagesFolder + "%d" % numberOfImages + ".jpg")
                else:
                    print("Created Image:", pathToImagesFolder + "%d" % numberOfImages + ".jpg")
                numberOfImages -= 1
                it_secs = 0

            # Display the resulting frame
            cv2.imshow('frameCopy', frameCopy)
        else:
            cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF
        if 27 == key:#Esc
            break
        elif 32 == key:
            if not cv2.imwrite(pathToImagesFolder+"%d"%numberOfImages+".jpg", frame):
                print("Error written images to:", pathToImagesFolder+"%d"%numberOfImages+".jpg")
            numberOfImages -= 1

        it += 1
        if 0==numberOfImages:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()