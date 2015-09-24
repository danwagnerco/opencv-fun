import numpy as np
import argparse
import cv2
import imutils # <~ some helpful functions we wrote

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# M1 = np.float32([[1, 0, 25], [0, 1, 50]])
# shifted_down = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
# cv2.imshow("Shifted Down and Right", shifted_down)
# cv2.waitKey(0)

# M2 = np.float32([[1, 0, -50], [0, 1, -90]])
# shifted_up = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
# cv2.imshow("Shifted Up and Left", shifted_up)
# cv2.waitKey(0)

shifted_down = imutils.translate(image, 25, 50)
cv2.imshow("Shifted Down and Right", shifted_down)
cv2.waitKey(0)

shifted_up = imutils.translate(image, -50, -90)
cv2.imshow("Shifted Up and Left", shifted_up)
cv2.waitKey(0)

