# Real-time Object Identification using YOLO Algorithm
## Complete Project Documentation

**Version:** 2.0.0  
**Last Updated:** December 15, 2025  
**Project:** Real-time Object Identification System

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage Guide](#usage-guide)
5. [Architecture](#architecture)
6. [API Reference](#api-reference)
7. [Configuration](#configuration)
8. [Troubleshooting](#troubleshooting)
9. [Development](#development)
10. [Deployment](#deployment)

---

## Overview

A modern, real-time object detection web application powered by YOLOv3 neural network. Detect objects in images, videos, and live webcam feeds through an intuitive web interface.

### Key Capabilities
- **Image Detection**: Upload and process images (JPG, PNG, GIF)
- **Video Detection**: Process video files (MP4, AVI, MOV, MKV)
- **Live Webcam**: Real-time detection using computer camera
- **80+ Object Classes**: Comprehensive COCO dataset support
- **Adjustable Confidence**: Fine-tune detection sensitivity

### Technology Stack
- **Backend**: Python 3.8+, Flask 2.0+
- **Computer Vision**: OpenCV 4.0+ with DNN module
- **Deep Learning**: YOLOv3 (COCO dataset)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

## Features

### 1. Image Detection
```
Upload → Detect → Download
```
- Drag-and-drop or browse to upload
- Real-time processing with YOLO
- Bounding boxes with confidence scores
- Download processed images

### 2. Video Detection
```
Upload → Process Frames → Download
```
- Frame-by-frame object detection
- Progress tracking during processing
- Annotated video output
- Unique object summary

### 3. Live Webcam Detection ⭐ NEW
```
Start → Stream → Detect → Stop
```
- Real-time MJPEG streaming
- Live confidence adjustment
- Object count overlay
- Thread-safe resource management
- Auto-cleanup on exit

### 4. User Interface
- Modern glassmorphism design
- Dark theme for comfortable viewing
- Responsive layout (desktop/tablet/mobile)
- Smooth animations and transitions
- Intuitive tab-based navigation

---

## Installation

### Prerequisites
```bash
# Required
- Python 3.8 or higher
- pip package manager
- Webcam (for live detection)

# Optional
- GPU with CUDA (for faster processing)
```

### Step 1: Install Dependencies
```bash
pip install flask opencv-python numpy werkzeug
```

### Step 2: Download YOLO Weights
Download `yolov3.weights` (248 MB) from:
- Official: https://pjreddie.com/darknet/yolo/
- Direct: https://pjreddie.com/media/files/yolov3.weights

Place in project root directory.

### Step 3: Verify Installation
```bash
# Check Python version
python --version  # Should be 3.8+

# Verify files
ls yolov3.weights yolov3.cfg coco.names app.py

# Test import
python -c "import cv2, flask, numpy; print('OK')"
```

---

## Usage Guide

### Starting the Application

```bash
# Navigate to project directory
cd c:\Users\INDIAN\Downloads\Yolo-object-detection-code

# Start Flask server
python app.py

# Expected output:
# Loading YOLO model...
# YOLO model loaded successfully! Ready to detect 80 object classes.
# Server starting on http://127.0.0.1:5000
```

### Accessing the Interface

Open browser and navigate to:
```
http://localhost:5000
```

### Mode 1: File Upload

**For Images:**
1. Click "Upload File" tab
2. Drag image or click to browse
3. Adjust confidence threshold (default: 50%)
4. Click "Process with AI"
5. View results side-by-side
6. Download processed image

**For Videos:**
1. Upload video file (max 100MB)
2. Set confidence threshold
3. Click "Process with AI"
4. Wait for processing (shows progress)
5. View annotated video
6. Download result

### Mode 2: Live Webcam

**Starting Detection:**
1. Click "Live Webcam" tab
2. Adjust confidence (optional)
3. Click "Start Webcam"
4. Allow camera access when prompted
5. View real-time detections

**During Detection:**
- Adjust confidence slider for live changes
- See object count in top-left corner
- Colored boxes around detected objects
- Labels with confidence scores

**Stopping Detection:**
1. Click "Stop Webcam"
2. Camera is released immediately
3. Can restart anytime

---

## Architecture

### System Architecture

```
┌─────────────────────────────────────┐
│         Browser (Client)            │
│  ┌─────────────────────────────┐   │
│  │  Upload Mode | Webcam Mode  │   │
│  └─────────────────────────────┘   │
└──────────────┬──────────────────────┘
               │ HTTP/MJPEG
┌──────────────▼──────────────────────┐
│       Flask Server (Backend)        │
│  ┌──────────────────────────────┐  │
│  │  API Routes & Controllers    │  │
│  ├──────────────────────────────┤  │
│  │  YOLO Detection Engine       │  │
│  ├──────────────────────────────┤  │
│  │  Video Streaming Generator   │  │
│  └──────────────────────────────┘  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│         YOLO Model (YOLOv3)         │
│  • yolov3.weights (248 MB)          │
│  • yolov3.cfg (configuration)       │
│  • coco.names (80 classes)          │
└─────────────────────────────────────┘
```

### Data Flow

**Image/Video Upload:**
```
Client → Upload File → Server
Server → YOLO Detection → Annotate
Server → Save Output → Return URL
Client → Display Results
```

**Webcam Streaming:**
```
Client → Start Request → Server
Server → Open Camera → Start Loop
Loop: Capture → Detect → Encode → Stream
Client → Display MJPEG Stream
Client → Stop Request → Server
Server → Release Camera → End Loop
```

### File Structure

```
Yolo-object-detection-code/
├── app.py                 # Main Flask application
├── yolov3.weights         # Pre-trained model (248 MB)
├── yolov3.cfg             # YOLO configuration
├── coco.names             # 80 object class labels
│
├── templates/
│   └── index.html         # Web interface
│
├── static/
│   ├── style.css          # Styling (18 KB)
│   └── script.js          # Frontend logic (14 KB)
│
├── uploads/               # Uploaded files (auto-created)
├── outputs/               # Processed results (auto-created)
├── images/                # Optional samples
│
└── Documentation/
    ├── README.md
    ├── QUICKSTART.md
    ├── WEBCAM_FEATURE.md
    ├── FEATURE_SUMMARY.md
    └── CHANGELOG.md
```

---

## API Reference

### Endpoints

#### `GET /`
Main web interface

**Response:** HTML page

---

#### `POST /upload`
Upload and process image/video

**Request:**
```
Content-Type: multipart/form-data
- file: Image or video file
- confidence: Float (0.0-1.0)
```

**Response:**
```json
{
  "success": true,
  "file_type": "image|video",
  "input_file": "timestamp_filename.ext",
  "output_file": "timestamp_detected.ext",
  "result": {
    "detected_objects": [...],
    "total_detections": 5
  }
}
```

---

#### `POST /webcam/start`
Start webcam detection

**Response:**
```json
{
  "success": true,
  "message": "Webcam started"
}
```

---

#### `POST /webcam/stop`
Stop webcam detection

**Response:**
```json
{
  "success": true,
  "message": "Webcam stopped"
}
```

---

#### `GET /webcam/feed?confidence=0.5`
Video stream (MJPEG)

**Parameters:**
- `confidence`: Detection threshold (0.0-1.0)

**Response:** Multipart MJPEG stream

---

#### `GET /webcam/status`
Check webcam status

**Response:**
```json
{
  "active": true|false
}
```

---

#### `GET /outputs/<filename>`
Download processed file

**Response:** File download

---

## Configuration

### Confidence Threshold

```python
# Range: 0.0 to 1.0
# Default: 0.5 (50%)

Low (0.0-0.3):    More detections, may include false positives
Medium (0.3-0.7): Balanced accuracy and recall
High (0.7-1.0):   Fewer detections, higher precision
```

### Webcam Settings

```python
# In app.py - generate_webcam_frames()
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Resolution width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Resolution height
camera.set(cv2.CAP_PROP_FPS, 30)            # Frame rate
```

### File Upload Limits

```python
# In app.py
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
app.config['ALLOWED_EXTENSIONS'] = {
    'png', 'jpg', 'jpeg', 'gif',  # Images
    'mp4', 'avi', 'mov', 'mkv'    # Videos
}
```

---

## Troubleshooting

### Common Issues

**1. Webcam Not Starting**
```
Error: "Failed to start webcam"

Solutions:
✓ Close other apps using camera (Zoom, Teams, Skype)
✓ Check browser camera permissions
✓ Refresh page and try again
✓ Restart browser
✓ Try different browser (Chrome recommended)
```

**2. No Objects Detected**
```
Problem: Webcam shows but no bounding boxes

Solutions:
✓ Lower confidence threshold to 30-40%
✓ Improve lighting conditions
✓ Move objects closer to camera
✓ Try common objects (phone, laptop, person)
✓ Check console for errors (F12)
```

**3. Slow Performance**
```
Problem: Low FPS or laggy detection

Solutions:
✓ Close resource-intensive applications
✓ Reduce video resolution
✓ Lower confidence threshold
✓ Use GPU acceleration (if available)
✓ Process smaller images/videos
```

**4. Import Errors**
```
Error: "ModuleNotFoundError: No module named 'cv2'"

Solution:
pip install opencv-python numpy flask werkzeug
```

**5. Weights File Missing**
```
Error: "Cannot find yolov3.weights"

Solution:
Download from: https://pjreddie.com/media/files/yolov3.weights
Place in project root directory
```

---

## Development

### Running in Debug Mode

```python
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5000)

# Features:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger
```

### Adding New Features

**Example: Custom Detection Zone**

```python
# In detect_objects_frame()
def detect_objects_frame(frame, confidence_threshold=0.5, zone=None):
    if zone:
        x1, y1, x2, y2 = zone
        frame_roi = frame[y1:y2, x1:x2]
        # Process only ROI
    # ... rest of detection
```

### Testing

```bash
# Test server startup
python app.py

# Test endpoints
curl http://localhost:5000/webcam/status

# Test file upload
curl -X POST -F "file=@test.jpg" -F "confidence=0.5" \
     http://localhost:5000/upload
```

---

## Deployment

### Production Checklist

- [ ] Set `debug=False` in app.py
- [ ] Use production WSGI server (Gunicorn, uWSGI)
- [ ] Configure HTTPS for camera access
- [ ] Set up proper logging
- [ ] Implement rate limiting
- [ ] Add authentication (if needed)
- [ ] Configure firewall rules
- [ ] Set up monitoring

### Using Gunicorn

```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With config
gunicorn -c gunicorn_config.py app:app
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## Performance Metrics

### Expected Performance

| Metric | Value |
|--------|-------|
| Image Detection | 1-3 seconds |
| Video Processing | 2-5 FPS |
| Webcam Streaming | 10-15 FPS (CPU) |
| Webcam Latency | <100ms |
| Model Load Time | 2-5 seconds |
| Memory Usage | 500MB - 1GB |

### Optimization Tips

1. **Use GPU**: 10-20x faster detection
2. **Reduce Resolution**: Faster processing
3. **Batch Processing**: For multiple files
4. **Caching**: Cache model in memory
5. **Async Processing**: For video files

---

## Supported Objects (80 Classes)

```
Person, Bicycle, Car, Motorcycle, Airplane, Bus, Train, Truck, Boat,
Traffic light, Fire hydrant, Stop sign, Parking meter, Bench, Bird,
Cat, Dog, Horse, Sheep, Cow, Elephant, Bear, Zebra, Giraffe,
Backpack, Umbrella, Handbag, Tie, Suitcase, Frisbee, Skis, Snowboard,
Sports ball, Kite, Baseball bat, Baseball glove, Skateboard, Surfboard,
Tennis racket, Bottle, Wine glass, Cup, Fork, Knife, Spoon, Bowl,
Banana, Apple, Sandwich, Orange, Broccoli, Carrot, Hot dog, Pizza,
Donut, Cake, Chair, Couch, Potted plant, Bed, Dining table, Toilet,
TV, Laptop, Mouse, Remote, Keyboard, Cell phone, Microwave, Oven,
Toaster, Sink, Refrigerator, Book, Clock, Vase, Scissors, Teddy bear,
Hair drier, Toothbrush
```

---

## License & Credits

### YOLO License
YOLOv3 is available under the YOLO license. See official documentation.

### Credits
- **YOLO**: Joseph Redmon
- **COCO Dataset**: Microsoft COCO team
- **OpenCV**: Open Source Computer Vision Library
- **Flask**: Pallets Projects

---

## Support & Contact

### Getting Help
- Check troubleshooting section
- Review documentation files
- Open issue on repository
- Check browser console (F12)

### Reporting Bugs
Include:
- Python version
- Browser and version
- Error messages
- Steps to reproduce

---

## Version History

**v2.0.0** (2025-12-15)
- Added live webcam detection
- Dual-mode interface
- Project cleanup
- Complete documentation

**v1.0.0** (Previous)
- Image/video upload detection
- Web interface
- Basic functionality

---

**Status: Production Ready ✅**  
**Documentation Complete**  
**Ready for Deployment**
