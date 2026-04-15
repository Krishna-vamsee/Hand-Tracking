# 🚀 Hand Tracking Elastic Physics System

A real-time **Computer Vision** project that uses **OpenCV** and **MediaPipe** to track hand gestures and simulate an elastic band using **physics (Hooke’s Law)**.

---

## 📌 Overview

This project detects hand movements through a webcam and creates an interactive **elastic band** between two hands using pinch gestures. The band behaves like a real object — stretching, contracting, and snapping back naturally.

---

## 🎯 Features

- ✋ Real-time hand tracking using MediaPipe  
- 🤏 Pinch gesture detection (thumb + index finger)  
- 🙌 Two-hand interaction  
- 🧵 Elastic band simulation using Hooke’s Law  
- 🎯 Smooth motion with damping effect  
- 💥 Snap-back effect when released  
- ⚡ FPS display for performance monitoring  

---

## 🔄 Workflow

Camera Input  
→ Hand Detection  
→ Landmark Tracking  
→ Pinch Detection  
→ Distance Calculation  
→ Physics Engine (Hooke’s Law + Damping)  
→ Elastic Visualization  

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **MediaPipe**
- **Math (Physics Simulation)**

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/krishnavamsee/hand-tracking.git
cd hand-tracking
