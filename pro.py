import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    read_ok, img = cap.read()
    if not read_ok:
        print("Failed to read from camera.")
        break

    img = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([40, 20, 50])
    upper_green = np.array([90, 255, 255])
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([179, 255, 50])
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 20, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_black = cv2.inRange(hsv, lower_black, upper_black)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    for mask, color, text, rect_color in [
        (mask_red, (0, 0, 255), "Red", (0, 0, 255)),
        (mask_green, (0, 255, 0), "Green", (0, 255, 0)),
        (mask_blue, (255, 0, 0), "Blue", (255, 0, 0)),
        (mask_black, (255, 255, 255), "Black", (255, 255, 255)),
        (mask_white, (0, 0, 0), "White", (0, 0, 0)),
    ]:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), rect_color, 2)
                cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Color Recognition Output', img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Cleanup resources
cap.release()
cv2.destroyAllWindows()
