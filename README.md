---

Real-Time Color Detection using OpenCV

This project is a Python-based real-time color detection application that uses OpenCV to detect colors from a live camera feed.
---
Colors Detected

The application is capable of detecting the following 20 colors:

1. Red


2. Green


3. Blue


4. Black


5. White


6. Yellow


7. Cyan


8. Magenta


9. Orange


10. Pink


11. Brown


12. Violet

13. Gray


14. Beige


15. Turquoise


16. Lime


17. Indigo


18. Peach


19. Lavender

20. Teal
---
Features

Detects predefined colors in real-time using the HSV color space.

Draws bounding rectangles around detected objects.

Displays labels indicating the detected color.

Easy to use with live camera input.
---
Demo

When you run the program:

Hold an object of a predefined color (red, green, blue, black, or white) in front of the camera.

The object will be highlighted with a rectangle in its respective color, and a label will be displayed above it.
---
Prerequisites

Make sure you have the following installed:

Python 3.x

OpenCV library (cv2)

NumPy library (numpy)

---
Code Explanation

HSV Color Space: The script uses the HSV (Hue, Saturation, Value) color space for detecting colors, which is more effective under varying lighting conditions than RGB.

Contours: The code uses OpenCV's findContours() function to detect contours of objects matching the specified color range.

Bounding Boxes and Labels: For each color detected, a bounding box is drawn around the object, and the color's name is displayed above it.

Contributing

Feel free to fork this project and submit pull requests if you have any improvements or bug fixes.
---
License

This project is open-source and available under the MIT License.
---
