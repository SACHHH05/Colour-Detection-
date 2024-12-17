---

Color Detection Using OpenCV

This project is a real-time color detection application that uses OpenCV to capture video from a webcam and detect various colors in the frame. The code processes the video stream and identifies the presence of 20 distinct colors, marking them with bounding boxes and labels.

Features

Detects 20 different colors in real-time from a webcam feed.

Uses HSV color space for better color detection under varying lighting conditions.

Displays bounding boxes around detected colors in the video frame.

Labels the detected colors on the video stream.


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



Prerequisites

Make sure to install the necessary libraries:

pip install opencv-python numpy

Installation

1. Clone the repository:

git clone https://github.com/your-username/color-detection.git


2. Install the required dependencies using pip (if not already installed):

pip install opencv-python numpy



Usage

1. Run the Python script to start detecting colors:

python color_detection.py


2. A webcam window will open. The script will continuously capture frames and attempt to identify the defined colors.


3. Colors that are detected in the video feed will be outlined with a bounding box and labeled with the name of the color.


4. To exit the application, press the 'x' key.



Code Explanation

HSV Color Space: The script uses the HSV (Hue, Saturation, Value) color space for detecting colors, which is more effective under varying lighting conditions than RGB.

Contours: The code uses OpenCV's findContours() function to detect contours of objects matching the specified color range.

Bounding Boxes and Labels: For each color detected, a bounding box is drawn around the object, and the color's name is displayed above it.


Contributing

Feel free to fork this project and submit pull requests if you have any improvements or bug fixes.

License

This project is open-source and available under the MIT License.


---
