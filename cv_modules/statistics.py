import cv2
import numpy as np


def image_statistics(image):
    gray = image if len(image.shape) == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    return {"width": width, "height": height, "channels": channels,
            "average_brightness": float(np.mean(gray)),
            "minimum_pixel_value": int(np.min(image)),
            "maximum_pixel_value": int(np.max(image))}
