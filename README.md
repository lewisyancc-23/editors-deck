# 🎛️ Editors Deck

> A DIY hardware controller for video editing, inspired by gaming controllers and dedicated creative interfaces.
> This project is still in progress. Stay tuned!

## 💡 Inspiration

The idea for Editors Deck came from combining two things I really enjoy: **video editing and gaming**.

I was inspired by dedicated creative controllers such as **TourBox**, which introduced me to the idea of using a physical controller to make editing workflows more intuitive and efficient.

As someone who enjoys gaming, I also wondered:

> **What if video editing could feel a little more like gaming? 🎮**

This project explores that idea by combining familiar gaming-style controls with video editing shortcuts.

Editors Deck is an independently developed student project and is not affiliated with or endorsed by TourBox.

---

## ✨ Features

- 🎮 Joystick-based controls
- 🔊 Volume control
- ⏪ Timeline navigation
- ✂️ Trim
- ✂️ Cut
- 📋 Copy
- 🗑️ Delete
- ▶️ Play / Pause
- 🖥️ LCD display
- 🔌 Arduino-based hardware
- 🐍 Python + PyAutoGUI automation

---

## 🎮 Controls

| Control | Function |
|---|---|
| Joystick ↑ | Volume Up |
| Joystick ↓ | Volume Down |
| Joystick ← | Timeline Backward |
| Joystick → | Timeline Forward |
| Button 1 | Trim |
| Button 2 | Cut |
| Button 3 | Copy |
| Button 4 | Delete |
| Double Press | Play / Pause |

---

## 🧠 System Overview

```text
Joystick + Buttons
        │
        ▼
   Arduino UNO
        │
   USB Serial
        │
        ▼
 Python Controller
    + PyAutoGUI
        │
        ▼
     CapCut
```
---

## 🔧 Hardware
- Arduino UNO
- Analog Joystick
- Push Buttons
- I2C 1602 LCD
- Breadboard
- Jumper Wires

---

## 💻 Software
- Arduino IDE
- Python
- PyAutoGUI

---

## 📁 Project Structure
```text
editors-deck/
│
├── hardware/
│   └── Arduino code
│
├── software/
│   └── Python code
│
├── media/
│   └── Project photos and demo
│
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started
