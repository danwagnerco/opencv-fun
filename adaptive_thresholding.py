import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

mean_threshold = cv2.adaptiveThreshold(blurred_image,
                                       255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       11,
                                       4)
cv2.imshow("Mean Threshold", mean_threshold)
cv2.waitKey(0)

gaussian_threshold = cv2.adaptiveThreshold(blurred_image,
                                           255,
                                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY_INV,
                                           15,
                                           3)
cv2.imshow("Gaussian Threshold", gaussian_threshold)
cv2.waitKey(0)

