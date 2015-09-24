import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# (h, w) = image.shape[:2] # <~ clever way to get the height and width!
# center = (w // 2, h // 2)

# m1 = cv2.getRotationMatrix2D(center, 45, 1.0)
# rotated_up = cv2.warpAffine(image, m1, (w, h))
# cv2.imshow("Rotated by 45 Degrees", rotated_up)
# cv2.waitKey(0)

# m2 = cv2.getRotationMatrix2D(center, -90, 1.0)
# rotated_down = cv2.warpAffine(image, m2, (w, h))
# cv2.imshow("Rotated by -90 Degrees", rotated_down)
# cv2.waitKey(0)

rotated_up = imutils.rotate(image, 45, None, 1.0)
cv2.imshow("Rotated by 45 Degrees", rotated_up)
cv2.waitKey(0)

rotated_down = imutils.rotate(image, -90, None, 1.0)
cv2.imshow("Rotated by -90 Degrees", rotated_down)
cv2.waitKey(0)


cv2.waitKey(0)
