import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Remember! OpenCV represents images as NumPy arrays with height first
# and width second, so the next line slices to extract a rectangular region
# starting at (240, 30) and ending at (335, 120)
cropped = image[30:120 , 240:335] # <~ y-axis values, then x-axis values
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)

