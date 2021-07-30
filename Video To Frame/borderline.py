import numpy as np
import cv2

# Lower and upper boundaries to choose skin color
boundaries = ([0, 120, 0], [150, 115, 120])


# Provides a borderline by comparing the edge detection with the skin color area.
def borderline(frame):
    lower, upper = boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask1 = cv2.inRange(frame, lower, upper)

    cannyMask = cv2.Canny(frame, 100, 200)
    mask = cv2.bitwise_or(mask1, cannyMask)
    output = cv2.bitwise_and(frame, frame, mask=mask)

    return output
