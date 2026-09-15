import cv2


def detect_shapes(image):
    result = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    found = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 300:
            continue
        perimeter = cv2.arcLength(contour, True)
        corners = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        vertices = len(corners)
        if vertices == 3:
            name = "Triangle"
        elif vertices == 4:
            x, y, width, height = cv2.boundingRect(corners)
            name = "Square" if 0.9 <= width / float(height) <= 1.1 else "Rectangle"
        else:
            name = "Circle"
        moments = cv2.moments(contour)
        if moments["m00"]:
            center = (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))
        else:
            center = tuple(corners[0][0])
        cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)
        cv2.putText(result, name, center, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        found.append(name)
    return result, found
