# 🏛️ Olympus Monitoring Dashboard & UI Animation

A system monitoring web dashboard built with Python and Flask that displays hardware telemetry and live network processes. The standout feature is a synchronized 3D splash screen animation of Zeus, paired with custom thunder sound effects.

---

## ⚡ Key Features

- **3D Zeus Splash Screen:** An interactive entry portal where 4 individual pieces of a Zeus image rotate through 3D CSS transforms and lock together with audio synchronization.
- **System Telemetry:** Real-time visualization of CPU and RAM usage using neon-gradient circular charts.
- **Firewall Interceptor Toggles:** Interactive switches to simulate blocking unauthorized ports, isolating malicious PIDs, and enabling secure DNSCrypt tunneling.
- **Payload Inspector:** A light client-side tool to scan text fields for basic XSS and SQL Injection (SQLi) signature patterns.
- **Crypto Toolkit:** Instant SHA-256 hash generator and high-entropy password creator leveraging native browser crypto engines.
- **Live Socket Sniffer Table:** Connects to the Flask backend to fetch process names, PIDs, local/foreign addresses, and their security risk analysis.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (Advanced 3D Transforms, Glassmorphism, Conic Gradients), JavaScript (Fetch API)
- **Cryptography:** Native Web Crypto API (SHA-256)

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/olympus-sentinel.git](https://github.com/YourUsername/olympus-sentinel.git)
   cd olympus-sentinel
Install requirements:

Bash


pip install -r requirements.txt
Run the Flask application:

Bash


python app.py
Open http://127.0.0.1:5000 in your web browser.

📂 Project Structure
Plaintext


olympus-sentinel/
├── app.py                     # Core Flask backend script
├── README.md                  # Project documentation
├── templates/
│   └── olympus.html           # Frontend dashboard & 3D Zeus animation
└── static/
    ├── sanctuary.jpg          # Dashboard background wallpaper
    ├── thunder.mp3            # Audio effect for the entry splash screen
    ├── zeus_top_left.png      # Top-left quadrant image
    ├── zeus_top_right.png     # Top-right quadrant image
    ├── zeus_bottom_left.png   # Bottom-left quadrant image
    └── zeus_bottom_right.png  # Bottom-right quadrant image
