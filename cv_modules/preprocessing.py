import cv2


def load_image(path):
    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"Could not load image: {path}")
    return image


def image_info(image):
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    return width, height, channels


def resize_image(image, width=600, height=400):
    return cv2.resize(image, (width, height))


def crop_image(image, x=0, y=0, width=None, height=None):
    height_limit, width_limit = image.shape[:2]
    width = width or width_limit - x
    height = height or height_limit - y
    return image[y:y + height, x:x + width]


def rotate_image(image, angle=90):
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    if angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    if angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    raise ValueError("Angle must be 90, 180, or 270")


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
