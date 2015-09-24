import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# ratio1 = 150.0 / image.shape[1]
# dim1 = (150, int(image.shape[0] * ratio1)) # <~ new (w, h) dimensions
# resized_width = cv2.resize(image, dim1, interpolation = cv2.INTER_AREA)
# # other interpolation options are cv2.INTER_LINEAR,
# # cv2.INTER_CUBIC and cv2.INTER_NEAREST
# cv2.imshow("Resized (Width)", resized_width)
# cv2.waitKey(0)

# ratio2 = 50.0 / image.shape[0]
# dim2 = (int(image.shape[1] * ratio2), 50) # <~ new (w, h) dimensions
# resized_height = cv2.resize(image, dim2, interpolation = cv2.INTER_AREA)
# cv2.imshow("Resized (Height)", resized_height)
# cv2.waitKey(0)

resized_width = imutils.resize(image, new_width = 150)
cv2.imshow("Resized (Width)", resized_width)
cv2.waitKey(0)

resized_height = imutils.resize(image, new_height = 50)
cv2.imshow("Resized (Height)", resized_height)
cv2.waitKey(0)

