# Webcam Face Detection
A Python application that performs real-time face detection through your webcam using OpenCV and Haar Cascade Classifiers. Supports front-facing and profile face detection with multiple cascade classifiers for improved accuracy.

## Features
- Real-time face detection using webcam feed
- Multiple face detection classifiers:
  - Front view detection
  - Front view alternative detection
  - Front view alternative 2 detection
  - Profile view detection
- Cross-platform support (Windows, Linux, macOS)
- Green rectangle highlighting of detected faces
- Image capture and save functionality
- Simple GUI with keyboard controls

## Requirements
```
Python 3.x
opencv-python
tkinter
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/webcam-face-detection.git
cd webcam-face-detection
```

2. Install dependencies:
```bash
pip install opencv-python
```

3. Ensure you have the required Haar Cascade classifier XML files in the `face_data/` directory:
- haarcascade_frontalface_default.xml
- haarcascade_frontalface_alt.xml
- haarcascade_frontalface_alt2.xml
- haarcascade_profileface.xml

## Usage
Run the script:
```bash
python webcam_scan_face.py
```

### Controls
- **ESC**: Close the application
- **SPACE**: Save the current frame as an image (when enabled)

## Project Structure
```
webcam-face-detection/
├── face_data/
│   ├── haarcascade_frontalface_default.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_alt2.xml
│   └── haarcascade_profileface.xml
├── webcam_scan_face.py
└── README.md
```

## Configuration
- Camera device selection can be modified by changing the device number in `cv2.VideoCapture()`
- Face detection parameters can be adjusted by modifying:
  - `scaleFactor`
  - `minNeighbors`
  - `minSize`
  - `flags`
- Image saving can be toggled using the `image_save` boolean variable

## Known Issues
- Camera device number may need adjustment depending on system configuration
- May require different camera init parameters for different operating systems
- Performance depends on system capabilities and lighting conditions

## Acknowledgements
- OpenCV team for computer vision framework
- Contributors to the Haar Cascade classifiers
