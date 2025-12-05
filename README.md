# Hand_Detection_Arvyax

# Virtual Hand Safety Sensor 
**A real-time hand intrusion detection system using only OpenCV – no MediaPipe, no deep learning**

[![demo](demo/demo.gif)](https://drive.google.com/file/d/1mhkouwmzEFNBW2NbCTRKB5FVGmcsCYL_/view?usp=drive_link) 
*(Live demo – hand approaches → WARNING → DANGER)*

### What This Project Actually Is
A **virtual safety zone** that detects when a human hand enters a forbidden area in front of a camera.

It behaves exactly like expensive industrial safety systems ($10,000–$50,000) from SICK, Keyence, or Pilz – but built with a $15 webcam and pure OpenCV running at **45–55 FPS on CPU**.

### Core Features (All Built from Scratch)
- Accurate hand detection using **optical flow + YCrCb skin filtering** (no background subtraction issues)
- Super reliable fingertip detection via **convexity defects**
- Full-hand intrusion fallback – even if fingers are flat or defects fail, it still triggers
- **3-state logic**:
  - **SAFE** – hand outside
  - **WARNING** – hand/finger touches the boundary
  - **DANGER** – any part enters the red zone
- Clean, centered red danger box with glowing feedback
- Huge, unmissable status text

### Why This Stands Out
- Zero external ML models → runs anywhere (even Raspberry Pi)
- No false negatives – uses both fingertip and full contour checking
- Real-time performance on CPU only
- Clean, readable, well-commented code (human-written, not copy-paste)

### Real Use Cases
- Robot cell safeguarding
- CNC/press machine guarding
- Interactive safety demos
- Teaching advanced computer vision concepts

### How to Run
```bash
pip install opencv-python numpy
python appFinal.py
