import cv2
import numpy as np


def gaussian_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def median_blur(image):
    return cv2.medianBlur(image, 5)


def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)


def binary_threshold(image):
    gray = image if len(image.shape) == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return result
