import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# mask = np.zeros(image.shape[:2], dtype = "uint8")
# (cx, cy) = (image.shape[1] // 2, image.shape[0] // 2) # < ~ center
# bottom_left = (cx - 75, cy - 75)
# top_right = (cx + 75, cy + 75)
# cv2.rectangle(mask, bottom_left, top_right, 255, -1)
# cv2.imshow("Mask", mask)
# cv2.waitKey(0)

# masked = cv2.bitwise_and(image, image, mask = mask)
# cv2.imshow("Mask applied to Image", masked)
# cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cx, cy), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

