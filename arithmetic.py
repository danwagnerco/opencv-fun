from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# print("==OpenCV math==")
# print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
# print("max of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# over = np.uint8([200]) + np.uint8([100])
# under = np.uint8([50]) - np.uint8([100])

# print("==NumPy math==")
# print(over)
# print(under)

M1 = np.ones(image.shape, dtype = "uint8") * 100
M2 = np.ones(image.shape, dtype = "uint8") * 50

added = cv2.add(image, M1)
cv2.imshow("Added", added)
cv2.waitKey(0)

subtracted = cv2.subtract(image, M2)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

