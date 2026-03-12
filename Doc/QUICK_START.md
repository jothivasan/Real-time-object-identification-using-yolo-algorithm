# Quick Start Guide

## Real-time Object Identification using YOLO Algorithm

Get up and running in **5 minutes**! ⚡

---

## 🚀 Quick Setup (Any System)

### Step 1: Install Python (if not installed)

**Check if Python is installed:**

```bash
python --version
# OR
python3 --version
```

**If not installed:**

- **Windows**: Download from [python.org](https://www.python.org/downloads/) ✓ Check "Add to PATH"
- **macOS**: `brew install python3`
- **Linux**: `sudo apt install python3 python3-pip`

---

### Step 2: Navigate to Project

**Windows:**

```cmd
cd "c:\path\to\Real time object identification using yolo algorithm\Real time object identification using yolo algorithm"
```

**macOS/Linux:**

```bash
cd "/path/to/Real time object identification using yolo algorithm/Real time object identification using yolo algorithm"
```

---

### Step 3: Install Dependencies

**Windows:**

```cmd
pip install -r requirements.txt
```

**macOS/Linux:**

```bash
pip3 install -r requirements.txt
```

**What gets installed:**

- Flask (web framework)
- OpenCV (computer vision)
- NumPy (numerical computing)
- Werkzeug (utilities)

---

### Step 4: Download YOLO Weights (if missing)

**Check if weights exist:**

```bash
# Windows
dir yolov3.weights

# macOS/Linux
ls -lh yolov3.weights
```

**If missing, download (248 MB):**

**Option A - Direct Download:**

1. Visit: https://pjreddie.com/media/files/yolov3.weights
2. Save to project folder

**Option B - Command Line:**

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

### Step 5: Run the Application

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

---

### Step 6: Open in Browser

**Open your browser and go to:**

```
http://localhost:5000
```

**You should see the YOLO Identifier interface!** 🎉

---

## 🎯 Quick Usage

### Upload Mode (Images/Videos)

1. **Click "Upload File" tab**
2. **Drag & drop** or **click to browse**
3. **Adjust confidence** (50% recommended)
4. **Click "Process with AI"**
5. **View results** and **download**

**Supported formats:**

- Images: JPG, PNG, GIF
- Videos: MP4, AVI, MOV
- Max size: 100 MB

---

### Live Webcam Mode

1. **Click "Live Webcam" tab**
2. **Click "Start Webcam"**
3. **Allow camera access** when prompted
4. **See real-time detections!**
5. **Click "Stop Webcam"** when done

**Tips:**

- Use good lighting
- Try common objects (phone, laptop, person, cup)
- Adjust confidence for more/fewer detections

---

## 🔧 Quick Troubleshooting

### Python not found?

- **Windows**: Use `py` instead of `python`
- **macOS/Linux**: Use `python3` instead of `python`

### Module not found?

```bash
pip install flask opencv-python numpy werkzeug
```

### Weights file missing?

Download from: https://pjreddie.com/media/files/yolov3.weights

### Port 5000 already in use?

Change port in `app.py` (last line):

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Webcam not working?

- Close other apps using camera
- Allow browser permissions
- Try Chrome browser
- Refresh the page

---

## 📱 Access from Other Devices

**Find your IP address:**

Windows:

```cmd
ipconfig
```

macOS/Linux:

```bash
ifconfig
```

**Access from phone/tablet:**

```
http://YOUR_IP_ADDRESS:5000
```

Example: `http://192.168.1.100:5000`

---

## 🎓 What Can It Detect?

**80+ objects including:**

**People & Animals:**
Person, Dog, Cat, Bird, Horse, Sheep, Cow, Elephant, Bear, Zebra, Giraffe

**Vehicles:**
Car, Bicycle, Motorcycle, Airplane, Bus, Train, Truck, Boat

**Electronics:**
Laptop, Cell phone, Mouse, Keyboard, TV, Remote

**Household:**
Chair, Couch, Bed, Dining table, Toilet, Bottle, Cup, Book, Clock

**Food:**
Banana, Apple, Sandwich, Orange, Pizza, Donut, Cake

**Sports:**
Sports ball, Baseball bat, Tennis racket, Skateboard, Surfboard

...and 40+ more!

---

## 📊 Performance Tips

### For Better Speed:

- Use smaller images/videos
- Lower confidence threshold
- Close other applications
- Consider GPU acceleration (advanced)

### For Better Accuracy:

- Use higher confidence (60-70%)
- Ensure good lighting
- Use clear, high-quality images
- Try different angles

---

## 🎯 Confidence Threshold Guide

| Setting                 | Detections | Accuracy | Use Case                  |
| ----------------------- | ---------- | -------- | ------------------------- |
| **Low (20-40%)**        | Many       | Lower    | Find all possible objects |
| **Medium (40-60%)**     | Balanced   | Good     | General use (recommended) |
| **High (60-80%)**       | Fewer      | Higher   | Only confident detections |
| **Very High (80-100%)** | Very few   | Highest  | Maximum precision         |

**Default: 50%** - Works well for most cases!

---

## 📁 Project Files

**Essential files:**

```
✓ app.py              - Main application
✓ yolov3.weights      - AI model (248 MB)
✓ yolov3.cfg          - Model configuration
✓ coco.names          - Object labels
✓ requirements.txt    - Dependencies
✓ templates/index.html - Web interface
✓ static/style.css    - Styling
✓ static/script.js    - Frontend logic
```

**Auto-created folders:**

```
uploads/  - Temporary uploaded files
outputs/  - Processed results
```

---

## 🆘 Need More Help?

**Detailed guides:**

- `INSTALLATION_GUIDE.md` - Complete installation for all systems
- `README.md` - Full feature documentation
- `PROJECT_DOCUMENTATION.md` - Technical details
- `DEPLOYMENT_GUIDE.md` - Production deployment

**Common issues:**

- Check browser console (Press F12)
- Verify all files are present
- Ensure Python 3.8+ is installed
- Check that port 5000 is available

---

## ✅ Quick Checklist

- [ ] Python 3.8+ installed
- [ ] Project folder opened in terminal
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] YOLO weights downloaded (yolov3.weights)
- [ ] Application running (`python app.py`)
- [ ] Browser opened to http://localhost:5000
- [ ] Interface loaded successfully

---

## 🎉 You're Ready!

**Try these first:**

1. Upload a photo of yourself (person detection)
2. Upload a photo of your desk (laptop, mouse, keyboard, cup)
3. Try the webcam feature
4. Experiment with confidence levels
5. Download your results

---

## 💡 Pro Tips

1. **Best results:** Good lighting + common objects + 50% confidence
2. **Faster processing:** Use smaller images (resize before upload)
3. **More detections:** Lower confidence to 30-40%
4. **Fewer false positives:** Raise confidence to 60-70%
5. **Webcam performance:** Close other apps, use good lighting

---

## 🌟 Features at a Glance

| Feature                   | Description                         | Status   |
| ------------------------- | ----------------------------------- | -------- |
| **Image Detection**       | Upload and detect objects in photos | ✅ Ready |
| **Video Detection**       | Process video files frame-by-frame  | ✅ Ready |
| **Live Webcam**           | Real-time detection using camera    | ✅ Ready |
| **80+ Objects**           | Comprehensive object recognition    | ✅ Ready |
| **Adjustable Confidence** | Fine-tune detection sensitivity     | ✅ Ready |
| **Download Results**      | Save processed files                | ✅ Ready |
| **Modern UI**             | Beautiful, intuitive interface      | ✅ Ready |

---

## 📞 Quick Support

**Application won't start?**

1. Check Python version: `python --version` (need 3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Verify weights file exists: `yolov3.weights` (248 MB)

**No detections showing?**

1. Lower confidence to 30%
2. Try common objects
3. Improve lighting
4. Check browser console (F12)

**Webcam issues?**

1. Close Zoom, Teams, Skype
2. Allow camera in browser
3. Try Chrome browser
4. Refresh page

---

**Enjoy detecting objects! 🎯**

For advanced features and deployment, see the other documentation files.

---

**Quick Links:**

- 📖 [Full Documentation](PROJECT_DOCUMENTATION.md)
- 💻 [Installation Guide](INSTALLATION_GUIDE.md)
- 🚀 [Deployment Guide](DEPLOYMENT_GUIDE.md)
- 📝 [README](README.md)
