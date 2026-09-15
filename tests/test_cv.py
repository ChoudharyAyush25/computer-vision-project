import cv2
import numpy as np
from cv_modules.preprocessing import grayscale, resize_image
from cv_modules.shape_detection import detect_shapes


def test_grayscale_has_one_channel():
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    assert len(grayscale(image).shape) == 2


def test_resize_dimensions():
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    assert resize_image(image, 50, 40).shape == (40, 50, 3)


def test_shape_detection_runs():
    image = np.zeros((200, 200, 3), dtype=np.uint8)
    cv2.rectangle(image, (30, 30), (150, 100), (255, 255, 255), -1)
    result, names = detect_shapes(image)
    assert result.shape == image.shape
    assert "Rectangle" in names
