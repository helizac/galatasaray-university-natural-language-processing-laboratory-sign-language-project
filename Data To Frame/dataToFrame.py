

import cv2
import numpy as np
import os

boundaries = [
    ([181, 228, 255], [255, 255, 255])
]
#,
    # ([25, 0, 75], [180, 38, 255])
def handsegment(frame):
    lower, upper = boundaries[0]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask1 = cv2.inRange(frame, lower, upper)

    # lower, upper = boundaries[1]
    # lower = np.array(lower, dtype="uint8")
    # upper = np.array(upper, dtype="uint8")
    # mask2 = cv2.inRange(frame, lower, upper)

    # for i,(lower, upper) in enumerate(boundaries):
    #   # create NumPy arrays from the boundaries
    #   lower = np.array(lower, dtype = "uint8")
    #   upper = np.array(upper, dtype = "uint8")

    #   # find the colors within the specified boundaries and apply
    #   # the mask
    #   if(i==0):
    #       print "Harish"
    #       mask1 = cv2.inRange(frame, lower, upper)
    #   else:
    #       print "Aadi"
    #       mask2 = cv2.inRange(frame, lower, upper)
    # mask = cv2.bitwise_or(mask1, mask2)
    output = cv2.bitwise_and(frame, frame, mask=mask1)
    # show the images
    cv2.imshow("images", mask1)
    cv2.imshow("images", output)
    return output

PATH = "C:\\1_DOSYALAR\\PROJELER\\PROJE_NLP_ISARET_DILI\\Videolar\\B\\"
files = os.listdir(PATH)

for file in files :
    
    pathVideo = PATH + str(file)
    videoName = str(file).strip(".mp4")

    # Playing video from file:
    cap = cv2.VideoCapture(pathVideo)

    try:
        if not os.path.exists(videoName):
            os.makedirs(videoName)
    except OSError:
        print ('Error: Creating directory of data')

    frameNumber = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    currentFrame = 0
    try:
        while(currentFrame < frameNumber):
            ret, frame = cap.read()
            # frame = handsegment(frame)
            frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            name = '.\\' + videoName +'\\frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
    except Exception as e:
        print(file + " hata var.\n" + f"Exception : {e}")
    print("\n\n")            

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




