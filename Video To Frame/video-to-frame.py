import cv2
import os
from os.path import exists
import argparse
from tqdm import tqdm

import borderline as bl


# Converts videos to jpeg format images
def convert(gesture_folder, target_folder):
    rootPath = os.getcwd()
    majorData = os.path.abspath(target_folder)

    if not exists(majorData):
        os.makedirs(majorData)

    gesture_folder = os.path.abspath(gesture_folder)

    os.chdir(gesture_folder)
    gestures = os.listdir(os.getcwd())

    print("Source Directory containing gestures: %s" % gesture_folder)
    print("Destination Directory containing frames: %s\n" % majorData)

    for gesture in tqdm(gestures, unit='actions', ascii=True):
        gesture_path = os.path.join(gesture_folder, gesture)
        os.chdir(gesture_path)

        gesture_frames_path = os.path.join(majorData, gesture)

        if not os.path.exists(gesture_frames_path):
            os.makedirs(gesture_frames_path)

        videos = os.listdir(os.getcwd())
        videos = [video for video in videos if (os.path.isfile(video))]

        for video in tqdm(videos, unit='videos', ascii=True):

            video_path = os.path.join(gesture_folder, gesture)
            os.chdir(video_path)

            video_frames_path = os.path.join(majorData, gesture)
            video_frames_path1 = os.path.join(video_frames_path, video)

            if not os.path.exists(video_frames_path1):
                os.makedirs(video_frames_path1)

            name = os.path.abspath(video)
            cap = cv2.cv2.VideoCapture(name)  # capturing input video
            frameCount = int(cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT))
            lastFrame = None

            os.chdir(video_frames_path1)
            count = 0

            while count <= frameCount:
                ret, frame = cap.read()  # extract frame
                if ret is False:
                    break
                framename = os.path.splitext(video)[0]
                framename = framename + "_frame_" + str(count) + ".jpeg"

                # In order to work flawlessly with Turkish characters
                framename = framename.replace("Ç", "C").replace("İ", "I").replace("Ö", "O").replace("Ş", "S").replace(
                    "ç", "c").replace("ı", "i").replace("ö", "o").replace("ş", "s")

                if not os.path.exists(framename):
                    frame = bl.borderline(frame)
                    frame = cv2.cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2GRAY)
                    lastFrame = frame
                    cv2.cv2.imwrite(framename, frame)

                if cv2.cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                count += 1

            while count <= frameCount:
                framename = os.path.splitext(video)[0]
                framename = framename + "_frame_" + str(count) + ".jpeg"

                # In order to work flawlessly with Turkish characters
                framename = framename.replace("Ç", "C").replace("İ", "I").replace("Ö", "O").replace("Ş", "S").replace(
                    "ç", "c").replace("ı", "i").replace("ö", "o").replace("ş", "s").replace("ğ", "g")

                if not os.path.exists(framename):
                    cv2.cv2.imwrite(framename, lastFrame)
                count += 1

            os.chdir(gesture_path)
            cap.release()
            cv2.cv2.destroyAllWindows()

    os.chdir(rootPath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Individual Frames from gesture videos.')
    parser.add_argument('gesture_folder', help='Path to folder containing folders of videos of different gestures.')
    parser.add_argument('target_folder', help='Path to folder where extracted frames should be kept.')
    args = parser.parse_args()
    convert(args.gesture_folder, args.target_folder)
