import numpy as np
import cv2

def translate(image, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))


def rotate(image, angle, non_center_rotation_point = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if non_center_rotation_point:
        center = non_center_rotation_point
    else:
        center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, matrix, (w, h))


def resize(image, new_height = None, new_width = None):
    dim = None
    (h, w) = image.shape[:2]

    if new_width is None and new_height:
        ratio = new_height / float(h)
        dim = (int(w * ratio), new_height)
    elif new_height is None and new_width:
        ratio = new_width / float(w)
        dim = (new_width, int(h * ratio))
    else:
        return image # <~ user did not specify a height or width change

    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

