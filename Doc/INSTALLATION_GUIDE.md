# Complete Installation Guide

## Real-time Object Identification using YOLO Algorithm

This guide will help you set up and run this project on **any system** (Windows, macOS, Linux).

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Platform-Specific Instructions](#platform-specific-instructions)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)

---

## 🖥️ System Requirements

### Minimum Requirements

- **Operating System**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+, or any Linux distribution
- **Python**: Version 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 1GB free space
- **Webcam**: Required for live detection feature (optional for image/video processing)
- **Internet**: Required for initial setup (downloading dependencies and model weights)

### Recommended Requirements

- **RAM**: 8GB or more
- **Processor**: Intel i5 or equivalent (or better)
- **GPU**: NVIDIA GPU with CUDA support (optional, for faster processing)
- **Browser**: Chrome, Edge, Firefox, or Safari (latest version)

---

## 🚀 Installation Steps

### Step 1: Install Python

#### Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```cmd
   python --version
   ```

#### macOS

```bash
# Using Homebrew (recommended)
brew install python3

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

---

### Step 2: Download the Project

**Option A: Download ZIP**

1. Download the project as a ZIP file
2. Extract to your desired location
3. Open terminal/command prompt in the extracted folder

**Option B: Clone Repository (if using Git)**

```bash
git clone <repository-url>
cd "Real time object identification using yolo algorithm"
```

---

### Step 3: Install Python Dependencies

Navigate to the project directory and run:

#### Windows

```cmd
cd "c:\path\to\Real time object identification using yolo algorithm\Real time object identification using yolo algorithm"
pip install -r requirements.txt
```

#### macOS/Linux

```bash
cd "/path/to/Real time object identification using yolo algorithm/Real time object identification using yolo algorithm"
pip3 install -r requirements.txt
```

**Dependencies that will be installed:**

- Flask 2.3.3 - Web framework
- opencv-python 4.8.0.76 - Computer vision library
- numpy 1.24.3 - Numerical computing
- Werkzeug 2.3.7 - WSGI utility library

---

### Step 4: Download YOLO Model Weights

The YOLO weights file (`yolov3.weights`) is **248 MB** and may or may not be included in your download.

#### Check if weights exist:

```bash
# Windows
dir yolov3.weights

# macOS/Linux
ls -lh yolov3.weights
```

#### If weights are missing, download them:

**Method 1: Direct Download**

1. Visit: https://pjreddie.com/media/files/yolov3.weights
2. Save the file to the project root directory
3. Ensure the filename is exactly `yolov3.weights`

**Method 2: Using Command Line**

Windows (PowerShell):

```powershell
Invoke-WebRequest -Uri "https://pjreddie.com/media/files/yolov3.weights" -OutFile "yolov3.weights"
```

macOS/Linux:

```bash
wget https://pjreddie.com/media/files/yolov3.weights
# OR
curl -O https://pjreddie.com/media/files/yolov3.weights
```

---

### Step 5: Verify Project Structure

Ensure your project directory contains these essential files:

```
Real time object identification using yolo algorithm/
├── app.py                    ✓ Main application
├── yolov3.weights            ✓ Model weights (248 MB)
├── yolov3.cfg                ✓ Model configuration
├── coco.names                ✓ Object class labels
├── requirements.txt          ✓ Dependencies
├── templates/
│   └── index.html           ✓ Web interface
├── static/
│   ├── style.css            ✓ Styling
│   └── script.js            ✓ Frontend logic
├── uploads/                  (auto-created)
└── outputs/                  (auto-created)
```

---

## 🎯 Platform-Specific Instructions

### Windows

#### Using Command Prompt

```cmd
# Navigate to project
cd "c:\Users\YourName\Downloads\Real time object identification using yolo algorithm\Real time object identification using yolo algorithm"

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### Using PowerShell

```powershell
# Navigate to project
Set-Location "c:\Users\YourName\Downloads\Real time object identification using yolo algorithm\Real time object identification using yolo algorithm"

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

**Common Windows Issues:**

- If `python` command not found, try `py` instead
- If `pip` not found, try `python -m pip` instead
- Ensure Python is added to PATH

---

### macOS

```bash
# Navigate to project
cd "/Users/YourName/Downloads/Real time object identification using yolo algorithm/Real time object identification using yolo algorithm"

# Install dependencies
pip3 install -r requirements.txt

# Run the application
python3 app.py
```

**macOS-Specific Notes:**

- Use `python3` and `pip3` instead of `python` and `pip`
- Grant camera permissions when prompted
- If using Apple Silicon (M1/M2), dependencies should work natively

---

### Linux (Ubuntu/Debian)

```bash
# Navigate to project
cd "/home/username/Downloads/Real time object identification using yolo algorithm/Real time object identification using yolo algorithm"

# Install system dependencies (if needed)
sudo apt install python3-dev python3-pip

# Install Python dependencies
pip3 install -r requirements.txt

# Run the application
python3 app.py
```

**Linux-Specific Notes:**

- May need to install `libopencv-dev` for OpenCV
- Ensure webcam permissions are granted
- Use `python3` instead of `python`

---

## ✅ Verification

### Step 1: Test Installation

Run this command to verify all dependencies are installed:

#### Windows

```cmd
python -c "import cv2, flask, numpy; print('✓ All dependencies installed successfully!')"
```

#### macOS/Linux

```bash
python3 -c "import cv2, flask, numpy; print('✓ All dependencies installed successfully!')"
```

### Step 2: Start the Application

#### Windows

```cmd
python app.py
```

#### macOS/Linux

```bash
python3 app.py
```

### Expected Output:

```
Loading YOLO model...
YOLO model loaded successfully! Ready to detect 80 object classes.

============================================================
Real-time Object Identification using YOLO Algorithm
============================================================
Server starting on http://127.0.0.1:5000
Press Ctrl+C to stop the server
============================================================

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
```

### Step 3: Access the Application

1. Open your web browser
2. Navigate to: **http://localhost:5000** or **http://127.0.0.1:5000**
3. You should see the YOLO Identifier interface

---

## 🔧 Troubleshooting

### Issue 1: Python Not Found

**Error:** `'python' is not recognized as an internal or external command`

**Solutions:**

- **Windows**: Reinstall Python and check "Add Python to PATH"
- **macOS/Linux**: Use `python3` instead of `python`
- **Alternative**: Use full path to Python executable

---

### Issue 2: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'cv2'` (or flask, numpy)

**Solutions:**

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or install individually
pip install flask opencv-python numpy werkzeug
```

---

### Issue 3: Weights File Not Found

**Error:** `FileNotFoundError: yolov3.weights not found`

**Solutions:**

1. Download weights from: https://pjreddie.com/media/files/yolov3.weights
2. Place in project root directory
3. Verify filename is exactly `yolov3.weights` (case-sensitive on Linux/macOS)

---

### Issue 4: Port Already in Use

**Error:** `Address already in use` or `Port 5000 is already allocated`

**Solutions:**

**Windows:**

```cmd
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**macOS/Linux:**

```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>
```

**Alternative:** Change port in `app.py`:

```python
# Change this line at the bottom of app.py
app.run(debug=True, host='0.0.0.0', port=5001)  # Use port 5001 instead
```

---

### Issue 5: Webcam Not Working

**Error:** Webcam doesn't start or shows black screen

**Solutions:**

1. **Close other applications** using the camera (Zoom, Teams, Skype)
2. **Grant browser permissions** when prompted
3. **Try different browser** (Chrome recommended)
4. **Check camera index** - Edit `app.py` and try different camera indices:
   ```python
   # In generate_webcam_frames() function
   camera = cv2.VideoCapture(0)  # Try 0, 1, 2, etc.
   ```
5. **Test camera separately:**
   ```bash
   python test_camera.py
   ```

---

### Issue 6: Slow Performance

**Problem:** Application is slow or laggy

**Solutions:**

1. **Close resource-intensive applications**
2. **Lower confidence threshold** (30-40%)
3. **Reduce video resolution** in code
4. **Use smaller images/videos**
5. **Consider GPU acceleration** (requires CUDA setup)

---

### Issue 7: OpenCV Installation Issues

**Error:** Issues installing `opencv-python`

**Solutions:**

**Windows:**

```cmd
pip install --upgrade pip
pip install opencv-python
```

**macOS:**

```bash
# If using Apple Silicon
pip3 install opencv-python

# If issues persist
brew install opencv
pip3 install opencv-python
```

**Linux:**

```bash
# Install system dependencies
sudo apt install python3-opencv
# OR
pip3 install opencv-python
```

---

## 🌐 Network Access (Optional)

To access the application from other devices on your network:

1. **Find your local IP address:**

   **Windows:**

   ```cmd
   ipconfig
   ```

   Look for "IPv4 Address" (e.g., 192.168.1.100)

   **macOS/Linux:**

   ```bash
   ifconfig
   # OR
   ip addr show
   ```

2. **Access from other devices:**
   - Open browser on another device (phone, tablet, another computer)
   - Navigate to: `http://YOUR_IP_ADDRESS:5000`
   - Example: `http://192.168.1.100:5000`

3. **Firewall Configuration:**
   - **Windows**: Allow Python through Windows Firewall
   - **macOS**: System Preferences → Security & Privacy → Firewall
   - **Linux**: Configure UFW or iptables

---

## 📱 Testing the Application

### Test 1: Image Detection

1. Click "Upload File" tab
2. Upload a test image (person, car, laptop, etc.)
3. Set confidence to 50%
4. Click "Process with AI"
5. Verify objects are detected with bounding boxes

### Test 2: Video Detection

1. Upload a short video file
2. Process and verify detection
3. Download the result

### Test 3: Live Webcam

1. Click "Live Webcam" tab
2. Click "Start Webcam"
3. Allow camera permissions
4. Verify real-time detection
5. Click "Stop Webcam"

---

## 🎓 Next Steps

After successful installation:

1. **Read the User Guide**: See `README.md` for usage instructions
2. **Explore Features**: Try all three detection modes
3. **Adjust Settings**: Experiment with confidence thresholds
4. **Check Documentation**: See `PROJECT_DOCUMENTATION.md` for advanced features

---

## 📞 Getting Help

If you encounter issues not covered here:

1. Check the **Troubleshooting** section above
2. Review `PROJECT_DOCUMENTATION.md`
3. Check browser console for errors (Press F12)
4. Ensure all files are present and dependencies installed
5. Verify Python version is 3.8 or higher

---

## ✅ Installation Checklist

- [ ] Python 3.8+ installed
- [ ] Project downloaded and extracted
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] YOLO weights downloaded (yolov3.weights - 248 MB)
- [ ] All project files present
- [ ] Application starts without errors
- [ ] Web interface accessible at http://localhost:5000
- [ ] Image upload works
- [ ] Webcam detection works (if webcam available)

---

**Congratulations! Your YOLO Object Detection system is ready to use! 🎉**

For detailed usage instructions, see `README.md` and `PROJECT_DOCUMENTATION.md`.
