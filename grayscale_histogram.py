from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.calcHist(images_as_list,
#              channels_as_list,
#              mask,
#              histogram_size_as_list,
#              pixel_range_as_list)

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Historgram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

