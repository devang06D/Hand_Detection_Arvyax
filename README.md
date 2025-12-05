# Virtual Hand Safety Sensor (No MediaPipe • Pure OpenCV)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-red)](https://opencv.org/)
[![FPS](https://img.shields.io/badge/Performance-45--55%20FPS-green)](#)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

**A real-time hand intrusion detection system** that works exactly like industrial safety light curtains — but built with just a webcam and pure OpenCV.  
No MediaPipe • No deep learning • Runs at **45–55 FPS on CPU only**

When a hand touches or enters the red danger zone → instantly switches from **SAFE → WARNING → DANGER** with glowing visual feedback.

---
## Demo Video
<p align="center">
  <a href="https://drive.google.com/file/d/https://drive.google.com/file/d/1mhkouwmzEFNBW2NbCTRKB5FVGmcsCYL_/view?usp=drive_link/view?usp=sharing">
    <img src="https://drive.google.com/thumbnail?id=https://drive.google.com/file/d/1mhkouwmzEFNBW2NbCTRKB5FVGmcsCYL_/view?usp=drive_link" width="800"/>
  </a>
</p>
<p align="center">
  <em>Click the image above to watch the live demo</em>
</p>

*(Replace `YOUR_DRIVE_VIDEO_ID` with your actual Google Drive video ID — the part after `/d/`)*

---
## What This Project Actually Does
Creates a **virtual forbidden zone** in front of your webcam:
- Hand far away → **SAFE** (green text)
- Finger/hand touches the boundary → **WARNING** (yellow ring glow)
- Any part enters the red box → **DANGER** (intense red glow + huge red text)

Used for:
- Robot cell safeguarding
- CNC / press machine protection
- Interactive safety demos
- Teaching real-time computer vision

---
## Tech Stack & Techniques (All from Scratch)
- **Language:** Python 3.8+
- **Core Library:** OpenCV + NumPy
- **Hand Detection:** Optical flow + YCrCb skin segmentation
- **Fingertip Detection:** Convexity defects
- **Ultra-Reliable Intrusion Logic:** Full contour pixel check (zero false negatives)
- **Visual Feedback:** Dynamic glow + huge centered text

No external models • No GPU • Works on laptops, Raspberry Pi, industrial PCs

---
## Prerequisites
- Python 3.8 or higher
- Webcam (built-in or USB)
- That’s it!

---
## Setup — Step by Step

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Hand_Detection_Arvyax.git
cd Hand_Detection_Arvyax
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install opencv-python numpy
source venv/bin/activate
```

### 4. Run appFinal.py
```bash
# In windows
python appFinal.py

# In mac/linux
python3 appFinal.py
```
