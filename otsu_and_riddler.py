from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray_image = cv2.imread(args["image"])
blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
cv2.imshow("Gray Image", gray_image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

