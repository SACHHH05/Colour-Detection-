# Color Detection using OpenCV

This project is a real-time color detection tool built using *Python* and *OpenCV*. It captures video from your webcam and detects 20 different colors live on the screen. Each color is shown with a bounding box and label.

---

## What It Does
- Detects *20 colors* from your webcam video feed.
- Draws *boxes* around the detected colors.
- Labels the color name on the video stream.
- Works well under different lighting using *HSV color space*.

---

## Colors Detected

- Red
- Green
- Blue
- Black
- White
- Yellow
- Cyan
- Magenta
- Orange
- Pink
- Brown
- Violet
- Gray
- Beige
- Turquoise
- Lime
- Indigo
- Peach
- Lavender
- Teal

---

## How It Works

- The script converts each video frame to *HSV color space*.
- It applies color masks to find areas with a specific color.
- It detects *contours* for those areas and draws bounding boxes.
- The color name is displayed on top of the box.

---

## Project File
- color_detector.py – Main script that runs color detection using OpenCV.

---

## How to Run

### 1. Install Requirements
pip install opencv-python numpy
### 2. Run the script
python color_detector.py
### 3.To exit
press the x key
