# Deployment Guide

## Real-time Object Identification using YOLO Algorithm

This guide covers deploying the YOLO Object Detection application to production environments.

---

## 📋 Table of Contents

1. [Production Preparation](#production-preparation)
2. [Local Network Deployment](#local-network-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Security Considerations](#security-considerations)
6. [Performance Optimization](#performance-optimization)

---

## 🔧 Production Preparation

### Pre-Deployment Checklist

- [ ] All dependencies installed
- [ ] YOLO weights file present (248 MB)
- [ ] Application tested locally
- [ ] Debug mode disabled
- [ ] Security measures implemented
- [ ] Backup created
- [ ] Monitoring configured

### Disable Debug Mode

**Important:** Never run Flask in debug mode in production!

Edit `app.py` and change the last line:

```python
# BEFORE (Development)
app.run(debug=True, host='0.0.0.0', port=5000)

# AFTER (Production)
app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## 🏠 Local Network Deployment

Deploy on your local network for access from multiple devices.

### Step 1: Configure Firewall

#### Windows

```cmd
# Allow Python through firewall
netsh advfirewall firewall add rule name="YOLO App" dir=in action=allow protocol=TCP localport=5000
```

#### macOS

```bash
# System Preferences → Security & Privacy → Firewall → Firewall Options
# Add Python to allowed applications
```

#### Linux (Ubuntu)

```bash
# Allow port 5000
sudo ufw allow 5000/tcp
sudo ufw reload
```

### Step 2: Find Your IP Address

#### Windows

```cmd
ipconfig
```

Look for "IPv4 Address" under your active network adapter.

#### macOS/Linux

```bash
ifconfig
# OR
ip addr show
```

### Step 3: Start the Server

```bash
python app.py
```

### Step 4: Access from Other Devices

From any device on the same network:

```
http://YOUR_IP_ADDRESS:5000
```

Example: `http://192.168.1.100:5000`

**Note:** Webcam feature requires HTTPS for remote access in most browsers.

---

## ☁️ Cloud Deployment

### Option 1: Heroku Deployment

#### Prerequisites

- Heroku account
- Heroku CLI installed

#### Step 1: Create Required Files

**Procfile:**

```
web: gunicorn app:app
```

**runtime.txt:**

```
python-3.9.18
```

**Update requirements.txt:**

```
Flask==2.3.3
opencv-python-headless==4.8.0.76
numpy==1.24.3
Werkzeug==2.3.7
gunicorn==21.2.0
```

#### Step 2: Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-yolo-app

# Deploy
git init
git add .
git commit -m "Initial deployment"
git push heroku main

# Open app
heroku open
```

**Note:** Free tier has limitations. Webcam may not work due to HTTPS requirements.

---

### Option 2: AWS EC2 Deployment

#### Step 1: Launch EC2 Instance

1. Choose Ubuntu Server 20.04 LTS
2. Instance type: t2.medium or larger
3. Configure security group:
   - SSH (22) - Your IP
   - HTTP (80) - Anywhere
   - HTTPS (443) - Anywhere
   - Custom TCP (5000) - Anywhere

#### Step 2: Connect and Setup

```bash
# Connect to instance
ssh -i your-key.pem ubuntu@your-instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip -y

# Clone/upload your project
# ... upload project files ...

# Install Python dependencies
cd /path/to/project
pip3 install -r requirements.txt

# Download YOLO weights
wget https://pjreddie.com/media/files/yolov3.weights
```

#### Step 3: Run with Gunicorn

```bash
# Install Gunicorn
pip3 install gunicorn

# Run application
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Step 4: Setup Nginx (Optional)

```bash
# Install Nginx
sudo apt install nginx -y

# Configure Nginx
sudo nano /etc/nginx/sites-available/yolo-app
```

**Nginx Configuration:**

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/yolo-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 5: Setup as Service (systemd)

```bash
sudo nano /etc/systemd/system/yolo-app.service
```

**Service Configuration:**

```ini
[Unit]
Description=YOLO Object Detection App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/project
ExecStart=/usr/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Start service
sudo systemctl daemon-reload
sudo systemctl start yolo-app
sudo systemctl enable yolo-app
sudo systemctl status yolo-app
```

---

### Option 3: Google Cloud Platform (GCP)

#### Using Google Cloud Run

**Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Download YOLO weights
RUN wget https://pjreddie.com/media/files/yolov3.weights

# Expose port
EXPOSE 8080

# Run application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
```

**Deploy:**

```bash
# Build and deploy
gcloud run deploy yolo-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🐳 Docker Deployment

### Step 1: Create Dockerfile

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Download YOLO weights if not present
RUN if [ ! -f yolov3.weights ]; then \
    wget https://pjreddie.com/media/files/yolov3.weights; \
    fi

# Create necessary directories
RUN mkdir -p uploads outputs

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Run application
CMD ["python", "app.py"]
```

### Step 2: Create docker-compose.yml

```yaml
version: "3.8"

services:
  yolo-app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./uploads:/app/uploads
      - ./outputs:/app/outputs
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
    devices:
      - /dev/video0:/dev/video0 # For webcam access (Linux)
```

### Step 3: Build and Run

```bash
# Build image
docker build -t yolo-object-detection .

# Run container
docker run -d -p 5000:5000 --name yolo-app yolo-object-detection

# OR use docker-compose
docker-compose up -d

# View logs
docker logs -f yolo-app

# Stop container
docker stop yolo-app

# Remove container
docker rm yolo-app
```

### Step 4: Docker Hub Deployment

```bash
# Tag image
docker tag yolo-object-detection yourusername/yolo-object-detection:latest

# Login to Docker Hub
docker login

# Push image
docker push yourusername/yolo-object-detection:latest

# Pull and run on any system
docker pull yourusername/yolo-object-detection:latest
docker run -d -p 5000:5000 yourusername/yolo-object-detection:latest
```

---

## 🔒 Security Considerations

### 1. Authentication (Optional)

Add basic authentication to protect your application:

```python
from flask import request, Response
from functools import wraps

def check_auth(username, password):
    return username == 'admin' and password == 'your-secure-password'

def authenticate():
    return Response(
        'Authentication required', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Apply to routes
@app.route('/')
@requires_auth
def index():
    return render_template('index.html')
```

### 2. HTTPS Configuration

For webcam access in production, HTTPS is required:

#### Using Let's Encrypt (Free SSL)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo certbot renew --dry-run
```

### 3. Rate Limiting

Prevent abuse with rate limiting:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/upload', methods=['POST'])
@limiter.limit("10 per minute")
def upload_file():
    # ... existing code ...
```

### 4. File Upload Security

Already implemented in `app.py`:

- File extension validation
- File size limits (100 MB)
- Secure filename handling
- Temporary file cleanup

### 5. Environment Variables

Store sensitive data in environment variables:

```python
import os

# In app.py
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
MAX_CONTENT_LENGTH = int(os.environ.get('MAX_UPLOAD_SIZE', 100 * 1024 * 1024))
```

Create `.env` file:

```
SECRET_KEY=your-super-secret-key-here
MAX_UPLOAD_SIZE=104857600
FLASK_ENV=production
```

---

## ⚡ Performance Optimization

### 1. Use Production WSGI Server

Never use Flask's built-in server in production!

#### Gunicorn (Recommended)

```bash
# Install
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With timeout for video processing
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 300 app:app
```

#### uWSGI

```bash
# Install
pip install uwsgi

# Run
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app --processes 4
```

### 2. GPU Acceleration

For significantly faster processing:

```python
# In app.py, add after loading the model:
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
```

**Requirements:**

- NVIDIA GPU
- CUDA Toolkit installed
- OpenCV compiled with CUDA support

### 3. Caching

Implement caching for repeated detections:

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=100)
def cached_detection(image_hash, confidence):
    # Detection logic
    pass
```

### 4. Async Processing

For video files, use background processing:

```python
from threading import Thread
from queue import Queue

processing_queue = Queue()

def process_video_async(video_path, output_path, confidence):
    # Process in background
    pass

@app.route('/upload', methods=['POST'])
def upload_file():
    # Add to queue instead of processing immediately
    processing_queue.put((video_path, output_path, confidence))
    return jsonify({'status': 'queued'})
```

### 5. Resource Limits

Configure resource limits:

```python
# In app.py
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# Cleanup old files
import time
import os

def cleanup_old_files(directory, max_age_hours=24):
    now = time.time()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            if os.stat(filepath).st_mtime < now - max_age_hours * 3600:
                os.remove(filepath)
```

---

## 📊 Monitoring and Logging

### 1. Application Logging

```python
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Use in code
app.logger.info('Detection started')
app.logger.error('Error processing video')
```

### 2. Performance Monitoring

```python
import time

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(request, 'start_time'):
        elapsed = time.time() - request.start_time
        app.logger.info(f'{request.method} {request.path} - {elapsed:.2f}s')
    return response
```

### 3. Health Check Endpoint

```python
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': net is not None,
        'timestamp': time.time()
    })
```

---

## 🔄 Continuous Deployment

### GitHub Actions Example

`.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /path/to/app
            git pull
            pip install -r requirements.txt
            sudo systemctl restart yolo-app
```

---

## 📝 Deployment Checklist

### Pre-Deployment

- [ ] Debug mode disabled
- [ ] Dependencies updated
- [ ] YOLO weights included
- [ ] Security measures implemented
- [ ] HTTPS configured (if needed)
- [ ] Firewall rules configured
- [ ] Backup created

### Post-Deployment

- [ ] Application accessible
- [ ] All features working
- [ ] Webcam detection tested
- [ ] File upload tested
- [ ] Performance acceptable
- [ ] Logs configured
- [ ] Monitoring active
- [ ] SSL certificate valid (if using HTTPS)

---

## 🆘 Troubleshooting Production Issues

### Issue: High Memory Usage

```bash
# Monitor memory
top
htop

# Restart application
sudo systemctl restart yolo-app

# Reduce workers
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

### Issue: Slow Response Times

- Enable GPU acceleration
- Reduce video resolution
- Implement caching
- Use CDN for static files
- Optimize confidence threshold

### Issue: Application Crashes

```bash
# Check logs
sudo journalctl -u yolo-app -f

# Check application logs
tail -f app.log

# Check system resources
df -h
free -m
```

---

## 📚 Additional Resources

- [Flask Deployment Documentation](https://flask.palletsprojects.com/en/latest/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Let's Encrypt](https://letsencrypt.org/)

---

**Your YOLO Object Detection application is now production-ready! 🚀**

For usage instructions, see `README.md` and `PROJECT_DOCUMENTATION.md`.
