from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
# cv2.waitKey(0)

channels = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("'Flattened' Color Historgram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

plt.show()
cv2.waitKey(0)

# Let's play with some 2D histograms
fig = plt.figure()

ax = fig.add_subplot(131)
hist_gb = cv2.calcHist([channels[1], channels[0]],
                       [0, 1],
                       None,
                       [32, 32],
                       [0, 256, 0, 256])
p = ax.imshow(hist_gb, interpolation = "nearest")
ax.set_title("2D Color Hist for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist_gr = cv2.calcHist([channels[1], channels[2]],
                       [0, 1],
                       None,
                       [32, 32],
                       [0, 256, 0, 256])
p = ax.imshow(hist_gr, interpolation = "nearest")
ax.set_title("2D Color Hist for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist_br = cv2.calcHist([channels[0], channels[2]],
                       [0, 1],
                       None,
                       [32, 32],
                       [0, 256, 0, 256])
p = ax.imshow(hist_br, interpolation = "nearest")
ax.set_title("2D Color Hist for B and R")
plt.colorbar(p)

plt.show()
cv2.waitKey(0)

print("2D histogram shape: {}, with {} values".format(hist_br.shape, hist_br.flatten().shape[0]))

# hist_3d = cv2.calcHist([image],
#                        [0, 1, 2],
#                        None,
#                        [8, 8, 8],
#                        [0, 256, 0, 256, 0, 256])
# print("3D histogram shape: {}, with {} values".format(hist_3d.shape, hist_3d.flatten().shape[0]))
# we can't visualize this histogram, but know it's an 8 x 8 x 8 joint

