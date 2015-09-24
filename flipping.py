import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flipped_horizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped_horizontally)
cv2.waitKey(0)

flipped_vertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped_vertically)
cv2.waitKey(0)

flipped_both = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and Horizontally", flipped_both)
cv2.waitKey(0)

