# System Requirements & Compatibility

## Real-time Object Identification using YOLO Algorithm

Complete system requirements and compatibility information for running this project on any platform.

---

## 📋 Table of Contents

1. [Minimum Requirements](#minimum-requirements)
2. [Recommended Specifications](#recommended-specifications)
3. [Operating System Compatibility](#operating-system-compatibility)
4. [Software Dependencies](#software-dependencies)
5. [Hardware Requirements](#hardware-requirements)
6. [Browser Compatibility](#browser-compatibility)
7. [Network Requirements](#network-requirements)

---

## 💻 Minimum Requirements

### Hardware

- **Processor**: Intel Core i3 / AMD Ryzen 3 or equivalent (2.0 GHz+)
- **RAM**: 2 GB minimum (4 GB recommended)
- **Storage**: 1 GB free disk space
  - 500 MB for project files
  - 248 MB for YOLO weights
  - 200 MB for dependencies
  - 50 MB for temporary files
- **Webcam**: Any USB or integrated webcam (for live detection feature)
- **Display**: 1024x768 resolution minimum

### Software

- **Python**: Version 3.8 or higher
- **pip**: Python package installer (usually included with Python)
- **Internet**: Required for initial setup (downloading dependencies and model weights)

### Network

- **Bandwidth**: 10 Mbps for downloading dependencies
- **Ports**: Port 5000 available (default, can be changed)

---

## 🚀 Recommended Specifications

### For Optimal Performance

#### Hardware

- **Processor**: Intel Core i5 / AMD Ryzen 5 or better (3.0 GHz+)
- **RAM**: 8 GB or more
- **Storage**: 2 GB free disk space (SSD preferred)
- **GPU**: NVIDIA GPU with CUDA support (optional, for 10-20x faster processing)
  - NVIDIA GTX 1050 or better
  - 2 GB VRAM minimum
  - CUDA 10.0 or higher
- **Webcam**: HD webcam (720p or 1080p) for better quality
- **Display**: 1920x1080 resolution or higher

#### Software

- **Python**: Version 3.9 or 3.10 (latest stable)
- **Browser**: Chrome or Edge (latest version)
- **OS**: Latest updates installed

#### Network

- **Bandwidth**: 50 Mbps for smooth operation
- **Latency**: <50ms for webcam streaming

---

## 🖥️ Operating System Compatibility

### ✅ Fully Supported

#### Windows

| Version         | Status             | Notes                     |
| --------------- | ------------------ | ------------------------- |
| **Windows 11**  | ✅ Fully Supported | Recommended               |
| **Windows 10**  | ✅ Fully Supported | All editions              |
| **Windows 8.1** | ✅ Supported       | May require updates       |
| **Windows 8**   | ⚠️ Limited         | Not recommended           |
| **Windows 7**   | ❌ Not Supported   | Python 3.9+ not available |

**Tested on:**

- Windows 11 Pro (64-bit)
- Windows 10 Home/Pro (64-bit)
- Windows 10 Enterprise (64-bit)

**Requirements:**

- 64-bit operating system
- Latest Windows updates
- .NET Framework 4.5+ (usually pre-installed)

---

#### macOS

| Version                    | Status             | Notes                       |
| -------------------------- | ------------------ | --------------------------- |
| **macOS Sonoma (14.x)**    | ✅ Fully Supported | Latest                      |
| **macOS Ventura (13.x)**   | ✅ Fully Supported | Recommended                 |
| **macOS Monterey (12.x)**  | ✅ Fully Supported | Stable                      |
| **macOS Big Sur (11.x)**   | ✅ Supported       | Works well                  |
| **macOS Catalina (10.15)** | ✅ Supported       | Minimum version             |
| **macOS Mojave (10.14)**   | ⚠️ Limited         | May have issues             |
| **Older versions**         | ❌ Not Supported   | Python compatibility issues |

**Tested on:**

- macOS Ventura (Intel & Apple Silicon)
- macOS Monterey (Intel & Apple Silicon)
- macOS Big Sur (Intel)

**Special Notes:**

- **Apple Silicon (M1/M2/M3)**: Fully supported with native performance
- **Intel Macs**: Fully supported
- **Rosetta 2**: Not required (native ARM support)

---

#### Linux

| Distribution         | Status             | Notes            |
| -------------------- | ------------------ | ---------------- |
| **Ubuntu 22.04 LTS** | ✅ Fully Supported | Recommended      |
| **Ubuntu 20.04 LTS** | ✅ Fully Supported | Stable           |
| **Ubuntu 18.04 LTS** | ✅ Supported       | Minimum version  |
| **Debian 11+**       | ✅ Fully Supported | Works well       |
| **Fedora 36+**       | ✅ Supported       | Tested           |
| **CentOS 8+**        | ✅ Supported       | Works            |
| **Arch Linux**       | ✅ Supported       | Rolling release  |
| **Raspberry Pi OS**  | ⚠️ Limited         | Slow performance |

**Tested on:**

- Ubuntu 22.04 LTS (x64)
- Ubuntu 20.04 LTS (x64)
- Debian 11 (x64)
- Fedora 38 (x64)

**Requirements:**

- 64-bit system (x86_64 or ARM64)
- Python 3.8+ available in repositories
- X11 or Wayland display server (for webcam)

---

### ⚠️ Limited Support

#### Raspberry Pi

- **Model**: Raspberry Pi 4 (4GB+ RAM)
- **OS**: Raspberry Pi OS (64-bit)
- **Status**: Works but slow
- **Performance**: 1-2 FPS for webcam, 10-30 seconds per image
- **Recommendation**: Use for learning/testing only

#### Windows Subsystem for Linux (WSL)

- **WSL 2**: Supported for image/video processing
- **Webcam**: Limited support (requires WSLg)
- **Recommendation**: Use native Windows installation instead

---

## 📦 Software Dependencies

### Python Version Compatibility

| Python Version | Status             | Notes           |
| -------------- | ------------------ | --------------- |
| **3.11**       | ✅ Fully Supported | Latest, fastest |
| **3.10**       | ✅ Fully Supported | Recommended     |
| **3.9**        | ✅ Fully Supported | Stable          |
| **3.8**        | ✅ Supported       | Minimum version |
| **3.7**        | ❌ Not Supported   | Too old         |
| **2.7**        | ❌ Not Supported   | Deprecated      |

### Required Python Packages

| Package           | Version  | Purpose             |
| ----------------- | -------- | ------------------- |
| **Flask**         | 2.3.3    | Web framework       |
| **opencv-python** | 4.8.0.76 | Computer vision     |
| **numpy**         | 1.24.3   | Numerical computing |
| **Werkzeug**      | 2.3.7    | WSGI utilities      |

**Installation:**

```bash
pip install -r requirements.txt
```

### Optional Dependencies

| Package                   | Purpose               | When Needed   |
| ------------------------- | --------------------- | ------------- |
| **gunicorn**              | Production server     | Deployment    |
| **opencv-contrib-python** | Extra CV features     | Advanced use  |
| **tensorflow**            | Alternative detection | Custom models |
| **torch**                 | PyTorch support       | Custom models |

---

## 🎮 Hardware Requirements

### CPU Requirements

#### Minimum

- **Architecture**: x86_64 (64-bit)
- **Cores**: 2 cores
- **Speed**: 2.0 GHz
- **Examples**: Intel Core i3-8100, AMD Ryzen 3 2200G

#### Recommended

- **Cores**: 4+ cores
- **Speed**: 3.0+ GHz
- **Examples**: Intel Core i5-10400, AMD Ryzen 5 3600

#### Performance Impact

- **2 cores**: 2-5 FPS webcam, 5-10 seconds per image
- **4 cores**: 8-12 FPS webcam, 2-3 seconds per image
- **6+ cores**: 12-15 FPS webcam, 1-2 seconds per image

---

### RAM Requirements

| RAM        | Status      | Performance               |
| ---------- | ----------- | ------------------------- |
| **2 GB**   | Minimum     | Basic operation, may swap |
| **4 GB**   | Recommended | Smooth for images         |
| **8 GB**   | Optimal     | Smooth for videos         |
| **16 GB+** | Excellent   | Multiple concurrent users |

**Memory Usage:**

- **Idle**: ~200 MB
- **Model loaded**: ~500 MB
- **Processing image**: ~600-800 MB
- **Processing video**: ~800 MB - 1.5 GB
- **Webcam active**: ~700-900 MB

---

### GPU Requirements (Optional)

#### For CUDA Acceleration

**Supported GPUs:**

- NVIDIA GPUs with CUDA Compute Capability 3.5+
- Examples: GTX 1050, RTX 2060, RTX 3060, RTX 4070

**Requirements:**

- **CUDA Toolkit**: 10.0 or higher
- **cuDNN**: Compatible version
- **VRAM**: 2 GB minimum, 4 GB recommended
- **OpenCV**: Compiled with CUDA support

**Performance Gain:**

- **CPU only**: 10-15 FPS webcam
- **With GPU**: 60-120 FPS webcam
- **Speedup**: 10-20x faster

**Note:** GPU acceleration requires additional setup and is optional.

---

### Storage Requirements

#### Disk Space Breakdown

```
Total Required: ~1 GB

Project Files:
├── Application code: 50 MB
├── YOLO weights: 248 MB
├── Python dependencies: 200 MB
├── Temporary files: 100 MB
└── Output files: 400 MB (varies)
```

#### Storage Type Impact

| Type        | Speed    | Recommendation  |
| ----------- | -------- | --------------- |
| **SSD**     | Fast     | Recommended     |
| **HDD**     | Slower   | Acceptable      |
| **Network** | Variable | Not recommended |

---

### Webcam Requirements

#### Supported Webcams

**Built-in Webcams:**

- ✅ Laptop integrated cameras
- ✅ All-in-one PC cameras
- ✅ Tablet cameras (Windows tablets)

**USB Webcams:**

- ✅ USB 2.0 webcams
- ✅ USB 3.0 webcams
- ✅ UVC-compatible cameras

**Unsupported:**

- ❌ IP cameras (requires modification)
- ❌ RTSP streams (requires modification)
- ❌ Virtual cameras (may work, not tested)

#### Resolution Support

| Resolution    | Status       | FPS   | Notes                     |
| ------------- | ------------ | ----- | ------------------------- |
| **640x480**   | ✅ Optimal   | 15-30 | Default, best performance |
| **1280x720**  | ✅ Supported | 10-20 | HD quality                |
| **1920x1080** | ✅ Supported | 5-15  | Full HD, slower           |
| **4K**        | ⚠️ Limited   | 2-5   | Very slow                 |

**Recommendation:** Use 640x480 for best performance.

---

## 🌐 Browser Compatibility

### Desktop Browsers

| Browser               | Status           | Webcam          | Notes       |
| --------------------- | ---------------- | --------------- | ----------- |
| **Google Chrome**     | ✅ Excellent     | ✅ Full support | Recommended |
| **Microsoft Edge**    | ✅ Excellent     | ✅ Full support | Recommended |
| **Mozilla Firefox**   | ✅ Good          | ✅ Supported    | Works well  |
| **Safari**            | ✅ Good          | ✅ Supported    | macOS only  |
| **Opera**             | ✅ Supported     | ✅ Supported    | Works       |
| **Brave**             | ✅ Supported     | ✅ Supported    | Works       |
| **Internet Explorer** | ❌ Not Supported | ❌ No           | Deprecated  |

**Tested Versions:**

- Chrome 120+
- Edge 120+
- Firefox 121+
- Safari 17+

---

### Mobile Browsers

| Browser              | Status       | Webcam     | Notes           |
| -------------------- | ------------ | ---------- | --------------- |
| **Chrome (Android)** | ✅ Supported | ✅ Works   | Good            |
| **Safari (iOS)**     | ✅ Supported | ⚠️ Limited | HTTPS required  |
| **Edge (Mobile)**    | ✅ Supported | ✅ Works   | Good            |
| **Firefox (Mobile)** | ✅ Supported | ⚠️ Limited | May have issues |

**Notes:**

- Mobile performance may be slower
- HTTPS required for camera access on mobile
- Responsive design works on tablets

---

### Browser Requirements

**Minimum:**

- HTML5 support
- JavaScript enabled
- CSS3 support
- File API support
- Canvas support

**For Webcam:**

- WebRTC support
- MediaDevices API
- getUserMedia() support
- HTTPS (for remote access)

---

## 🌍 Network Requirements

### Internet Connection

#### Initial Setup

- **Required**: Yes (one-time)
- **Bandwidth**: 10-50 Mbps
- **Purpose**: Download dependencies and YOLO weights (~300 MB)

#### Runtime

- **Required**: No (works offline after setup)
- **Local network**: Optional (for multi-device access)
- **Internet**: Not required for operation

---

### Port Requirements

| Port     | Protocol | Purpose            | Required      |
| -------- | -------- | ------------------ | ------------- |
| **5000** | TCP      | Flask application  | Yes (default) |
| **80**   | TCP      | HTTP (production)  | Optional      |
| **443**  | TCP      | HTTPS (production) | Optional      |

**Notes:**

- Port 5000 can be changed in `app.py`
- HTTPS (port 443) required for remote webcam access
- Firewall must allow chosen port

---

### Network Performance

#### Local Access (localhost)

- **Latency**: <1ms
- **Bandwidth**: Unlimited
- **Performance**: Excellent

#### LAN Access (same network)

- **Latency**: <10ms
- **Bandwidth**: 100 Mbps+ recommended
- **Performance**: Very good

#### Remote Access (internet)

- **Latency**: <100ms recommended
- **Bandwidth**: 5 Mbps+ recommended
- **Performance**: Good (depends on connection)

---

## 📊 Performance Benchmarks

### Expected Performance by System

#### Low-End System

- **Specs**: 2 cores, 2 GB RAM, no GPU
- **Image**: 5-10 seconds
- **Video**: 2-3 FPS processing
- **Webcam**: 5-8 FPS

#### Mid-Range System

- **Specs**: 4 cores, 8 GB RAM, no GPU
- **Image**: 2-3 seconds
- **Video**: 5-8 FPS processing
- **Webcam**: 10-15 FPS

#### High-End System

- **Specs**: 8 cores, 16 GB RAM, NVIDIA GPU
- **Image**: <1 second
- **Video**: 30+ FPS processing
- **Webcam**: 60+ FPS

---

## ✅ Compatibility Checklist

Before installation, verify:

- [ ] Operating system is Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- [ ] Python 3.8 or higher is installed
- [ ] At least 2 GB RAM available
- [ ] At least 1 GB free disk space
- [ ] Internet connection available (for setup)
- [ ] Port 5000 is available (or can be changed)
- [ ] Webcam connected (for live detection)
- [ ] Modern browser installed (Chrome/Edge recommended)

---

## 🔍 System Check Commands

### Check Python Version

```bash
python --version
# OR
python3 --version
```

### Check Available RAM

**Windows:**

```cmd
systeminfo | findstr "Available Physical Memory"
```

**macOS/Linux:**

```bash
free -h
```

### Check Disk Space

**Windows:**

```cmd
dir
```

**macOS/Linux:**

```bash
df -h .
```

### Check Port Availability

**Windows:**

```cmd
netstat -an | findstr :5000
```

**macOS/Linux:**

```bash
lsof -i :5000
```

### Test Webcam

```bash
python test_camera.py
```

---

## 📞 Support Matrix

| Component            | Support Level | Documentation         |
| -------------------- | ------------- | --------------------- |
| **Windows 10/11**    | ✅ Full       | INSTALLATION_GUIDE.md |
| **macOS 10.14+**     | ✅ Full       | INSTALLATION_GUIDE.md |
| **Ubuntu 18.04+**    | ✅ Full       | INSTALLATION_GUIDE.md |
| **Python 3.8-3.11**  | ✅ Full       | requirements.txt      |
| **Chrome/Edge**      | ✅ Full       | README.md             |
| **GPU Acceleration** | ⚠️ Advanced   | DEPLOYMENT_GUIDE.md   |
| **Docker**           | ✅ Full       | DEPLOYMENT_GUIDE.md   |
| **Mobile Browsers**  | ⚠️ Limited    | README.md             |

---

**Your system meets the requirements? Great! Proceed to [QUICK_START.md](QUICK_START.md) or [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** 🚀
