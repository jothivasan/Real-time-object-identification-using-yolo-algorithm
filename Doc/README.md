# Real-time Object Identification using YOLO Algorithm

A **cross-platform**, web-based real-time object detection application using YOLOv3 (You Only Look Once) algorithm with Flask backend. Works on **Windows, macOS, and Linux**!

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/opencv-4.8.0-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/license-YOLO-yellow.svg)](https://pjreddie.com/darknet/yolo/)

---

## 🌟 Features

- 🖼️ **Image Detection** - Upload and detect objects in images (JPG, PNG, GIF)
- 🎥 **Video Detection** - Process videos with object detection (MP4, AVI, MOV)
- 📹 **Live Webcam Detection** - Real-time object detection using webcam
- 🎯 **80+ Object Classes** - Detects people, vehicles, animals, electronics, food, and more
- ⚙️ **Adjustable Confidence** - Control detection sensitivity (0-100%)
- 💾 **Download Results** - Save processed images and videos
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux
- 🎨 **Modern UI** - Beautiful, intuitive web interface with dark theme
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile devices

---

## 🚀 Quick Start

### For Impatient Users (5 Minutes Setup)

```bash
# 1. Navigate to project folder
cd "path/to/Real time object identification using yolo algorithm/Real time object identification using yolo algorithm"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download YOLO weights (if missing) - 248 MB
# Windows PowerShell:
Invoke-WebRequest -Uri "https://pjreddie.com/media/files/yolov3.weights" -OutFile "yolov3.weights"
# macOS/Linux:
wget https://pjreddie.com/media/files/yolov3.weights

# 4. Run the application
python app.py

# 5. Open browser to http://localhost:5000
```

**📖 Need detailed instructions?** See **[QUICK_START.md](QUICK_START.md)**

---

## 💻 System Requirements

### Minimum Requirements

- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+, or any modern Linux
- **Python**: 3.8 or higher
- **RAM**: 2 GB (4 GB recommended)
- **Storage**: 1 GB free space
- **Webcam**: Any USB or integrated webcam (for live detection)
- **Browser**: Chrome, Edge, Firefox, or Safari (latest version)

### Recommended for Best Performance

- **RAM**: 8 GB or more
- **Processor**: Intel i5 / AMD Ryzen 5 or better
- **GPU**: NVIDIA GPU with CUDA (optional, for 10-20x faster processing)

**📊 Full compatibility details:** See **[SYSTEM_REQUIREMENTS.md](SYSTEM_REQUIREMENTS.md)**

---

## 📦 Installation

### Step 1: Install Python

**Windows:**

- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation

**macOS:**

```bash
brew install python3
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Install Dependencies

**Windows:**

```cmd
pip install -r requirements.txt
```

**macOS/Linux:**

```bash
pip3 install -r requirements.txt
```

**What gets installed:**

- Flask 2.3.3 - Web framework
- opencv-python 4.8.0.76 - Computer vision library
- numpy 1.24.3 - Numerical computing
- Werkzeug 2.3.7 - WSGI utilities

### Step 3: Download YOLO Model Weights

The YOLO weights file (248 MB) may not be included. Download it:

**Direct Download:**
https://pjreddie.com/media/files/yolov3.weights

**Or use command line:**

**Windows (PowerShell):**

```powershell
Invoke-WebRequest -Uri "https://pjreddie.com/media/files/yolov3.weights" -OutFile "yolov3.weights"
```

**macOS/Linux:**

```bash
wget https://pjreddie.com/media/files/yolov3.weights
# OR
curl -O https://pjreddie.com/media/files/yolov3.weights
```

**📖 Detailed installation for all platforms:** See **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)**

---

## 🎯 Usage

### Starting the Application

**Windows:**

```cmd
python app.py
```

**macOS/Linux:**

```bash
python3 app.py
```

**Expected Output:**

```
Loading YOLO model...
YOLO model loaded successfully! Ready to detect 80 object classes.

============================================================
Real-time Object Identification using YOLO Algorithm
============================================================
Server starting on http://127.0.0.1:5000
Press Ctrl+C to stop the server
============================================================
```

### Accessing the Interface

Open your browser and navigate to:

```
http://localhost:5000
```

### Mode 1: Upload File (Images/Videos)

1. Click **"Upload File"** tab
2. Drag & drop or click to browse
3. Adjust confidence threshold (default: 50%)
4. Click **"Process with AI"**
5. View results and download

**Supported Formats:**

- **Images**: JPG, PNG, GIF
- **Videos**: MP4, AVI, MOV, MKV
- **Max Size**: 100 MB

### Mode 2: Live Webcam Detection

1. Click **"Live Webcam"** tab
2. Adjust confidence (optional)
3. Click **"Start Webcam"**
4. Allow camera permissions
5. See real-time detections!
6. Click **"Stop Webcam"** when done

**Tips for Best Results:**

- Use good lighting
- Try common objects (phone, laptop, person, cup)
- Adjust confidence: 50% works well for most cases

## Project Structure

```
├── app.py                  # Main Flask application
├── yolov3.weights          # YOLO model weights (248 MB)
├── yolov3.cfg              # YOLO configuration
├── coco.names              # Object class labels (80 classes)
├── templates/
│   └── index.html          # Web interface
├── static/
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── uploads/                # Temporary uploaded files
├── outputs/                # Processed results
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Supported File Formats

- **Images**: JPG, PNG, GIF
- **Videos**: MP4, AVI, MOV, MKV
- **Max file size**: 100 MB

## Detectable Objects (80 Classes)

**Common Objects**: Person, Car, Bicycle, Motorcycle, Dog, Cat, Bird, Horse, Laptop, Cell phone, Mouse, Keyboard, Chair, Couch, Bed, Dining table, TV, Bottle, Cup, Book, Clock

**Vehicles**: Airplane, Bus, Train, Truck, Boat

**Animals**: Sheep, Cow, Elephant, Bear, Zebra, Giraffe

**Food**: Banana, Apple, Sandwich, Orange, Pizza, Donut, Cake

**Sports**: Sports ball, Baseball bat, Tennis racket, Skateboard, Surfboard

...and 40+ more!

---

## 📚 Complete Documentation

This project includes comprehensive documentation for all platforms and use cases:

| Document                                                 | Description                      | Best For                              |
| -------------------------------------------------------- | -------------------------------- | ------------------------------------- |
| **[QUICK_START.md](QUICK_START.md)**                     | 5-minute setup guide             | Getting started quickly               |
| **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)**       | Detailed installation for all OS | First-time setup, troubleshooting     |
| **[SYSTEM_REQUIREMENTS.md](SYSTEM_REQUIREMENTS.md)**     | Hardware/software compatibility  | Checking if your system is compatible |
| **[PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)** | Complete technical documentation | Advanced users, API reference         |
| **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**           | Production deployment guide      | Deploying to cloud/production         |
| **README.md** (this file)                                | Overview and quick reference     | General information                   |

**📖 New to this project?** Start with [QUICK_START.md](QUICK_START.md)  
**📊 Need detailed setup?** See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)  
**🚀 Ready to deploy?** Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## Troubleshooting

### Webcam not working

- Close other applications using the camera
- Allow camera permissions in browser
- Use Chrome or Edge browser
- Refresh the page

### No detections

- Lower confidence threshold to 30-40%
- Ensure good lighting
- Move closer to camera
- Try common objects

### Slow performance

- Close other applications
- Reduce video resolution
- Lower confidence threshold

## API Endpoints

| Method | Endpoint          | Description             |
| ------ | ----------------- | ----------------------- |
| GET    | `/`               | Web interface           |
| POST   | `/upload`         | Upload and process file |
| POST   | `/webcam/start`   | Start webcam detection  |
| POST   | `/webcam/stop`    | Stop webcam detection   |
| GET    | `/webcam/feed`    | Video stream            |
| GET    | `/webcam/status`  | Check webcam status     |
| GET    | `/outputs/<file>` | Download processed file |

## Performance

- **Image Processing**: 1-3 seconds
- **Video Processing**: 2-5 FPS
- **Webcam Detection**: 10-15 FPS
- **Latency**: <100ms

## Technologies Used

- **Backend**: Flask (Python)
- **Object Detection**: YOLOv3 with OpenCV
- **Frontend**: HTML5, CSS3, JavaScript
- **Computer Vision**: OpenCV (cv2)

## License

This project uses YOLOv3 which is available under the YOLO license. Please refer to the original YOLO documentation for more details.

## Credits

- YOLOv3: Joseph Redmon (https://pjreddie.com/darknet/yolo/)
- COCO Dataset: Common Objects in Context

## Version

**Current Version**: 2.0.0  
**Status**: Production Ready ✅

---

**For detailed documentation**, see `PROJECT_DOCUMENTATION.md`
