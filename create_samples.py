from pathlib import Path
import cv2
import numpy as np

Path("images").mkdir(exist_ok=True)
sample = np.zeros((400, 600, 3), dtype=np.uint8)
sample[:] = (210, 210, 210)
cv2.circle(sample, (150, 200), 80, (40, 120, 220), -1)
cv2.rectangle(sample, (300, 100), (520, 300), (60, 180, 80), -1)
cv2.imwrite("images/sample.jpg", sample)
shapes = np.zeros((500, 700, 3), dtype=np.uint8)
cv2.rectangle(shapes, (40, 60), (190, 210), (255, 255, 255), -1)
cv2.rectangle(shapes, (250, 50), (420, 220), (255, 255, 255), -1)
cv2.circle(shapes, (560, 140), 85, (255, 255, 255), -1)
triangle = np.array([[170, 400], [70, 250], [270, 250]], np.int32)
cv2.drawContours(shapes, [triangle], -1, (255, 255, 255), -1)
cv2.imwrite("images/shapes.jpg", shapes)
