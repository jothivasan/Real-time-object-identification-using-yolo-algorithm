from flask import Flask, render_template, request, jsonify, send_file, url_for, Response
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename
import time
import base64
from pathlib import Path
import threading

app = Flask(__name__)

# Webcam state management
webcam_active = False
webcam_lock = threading.Lock()
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'mkv'}

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)

# Load YOLO model (load once at startup)
print("Loading YOLO model...")
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Load class labels
with open('coco.names', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Get output layer names
layer_names = net.getLayerNames()
unconnected = net.getUnconnectedOutLayers()
if len(unconnected.shape) == 1:
    output_layers = [layer_names[i-1] for i in unconnected]
else:
    output_layers = [layer_names[i[0]-1] for i in unconnected]

# Generate random colors for each class
colors = np.random.uniform(0, 255, size=(len(labels), 3))

print(f"YOLO model loaded successfully! Ready to detect {len(labels)} object classes.")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def is_video(filename):
    video_extensions = {'mp4', 'avi', 'mov', 'mkv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in video_extensions

def detect_objects_image(image_path, output_path, confidence_threshold=0.5):
    """Detect objects in an image"""
    image = cv2.imread(image_path)
    height, width, channels = image.shape
    
    # Detecting objects
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)
    
    # Process detections
    boxes = []
    confidences = []
    class_ids = []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Apply Non-Maximum Suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)
    
    # Draw bounding boxes
    font = cv2.FONT_HERSHEY_SIMPLEX
    detected_objects = []
    
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(labels[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            label_text = f"{label} {confidence:.2f}"
            cv2.putText(image, label_text, (x, y - 5), font, 0.6, color, 2)
            
            detected_objects.append({
                'label': label,
                'confidence': f"{confidence:.2%}",
                'bbox': [x, y, w, h]
            })
    
    cv2.imwrite(output_path, image)
    
    return {
        'detected_objects': detected_objects,
        'total_detections': len(detected_objects)
    }

def detect_objects_video(video_path, output_path, confidence_threshold=0.5):
    """Detect objects in a video"""
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        return {'error': 'Could not open video file'}
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    frame_count = 0
    all_detected_objects = set()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        
        # Detect objects in frame
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outputs = net.forward(output_layers)
        
        boxes = []
        confidences = []
        class_ids = []
        
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > confidence_threshold:
                    center_x = int(detection[0] * frame_width)
                    center_y = int(detection[1] * frame_height)
                    w = int(detection[2] * frame_width)
                    h = int(detection[3] * frame_height)
                    
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(labels[class_ids[i]])
                confidence = confidences[i]
                color = colors[class_ids[i]]
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                label_text = f"{label} {confidence:.2f}"
                cv2.putText(frame, label_text, (x, y - 5), font, 0.6, color, 2)
                
                all_detected_objects.add(label)
        
        # Add progress indicator
        progress_text = f"Frame: {frame_count}/{total_frames}"
        cv2.putText(frame, progress_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        out.write(frame)
    
    cap.release()
    out.release()
    
    return {
        'detected_objects': sorted(list(all_detected_objects)),
        'total_frames': frame_count,
        'duration': f"{frame_count/fps:.2f}s"
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
    
    # Get confidence threshold from request
    confidence_threshold = float(request.form.get('confidence', 0.5))
    
    # Save uploaded file
    filename = secure_filename(file.filename)
    timestamp = int(time.time())
    input_filename = f"{timestamp}_{filename}"
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
    file.save(input_path)
    
    # Determine output filename
    file_ext = filename.rsplit('.', 1)[1].lower()
    output_filename = f"{timestamp}_detected.{file_ext}"
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
    
    try:
        # Process based on file type
        if is_video(filename):
            result = detect_objects_video(input_path, output_path, confidence_threshold)
            file_type = 'video'
        else:
            result = detect_objects_image(input_path, output_path, confidence_threshold)
            file_type = 'image'
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            'file_type': file_type,
            'input_file': input_filename,
            'output_file': output_filename,
            'result': result
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/outputs/<filename>')
def get_output(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename))

@app.route('/uploads/<filename>')
def get_upload(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

def detect_objects_frame(frame, confidence_threshold=0.5):
    """Detect objects in a single frame and return the annotated frame"""
    height, width, channels = frame.shape
    
    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)
    
    # Process detections
    boxes = []
    confidences = []
    class_ids = []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Apply Non-Maximum Suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)
    
    # Draw bounding boxes
    font = cv2.FONT_HERSHEY_SIMPLEX
    detected_count = 0
    
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(labels[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            label_text = f"{label} {confidence:.2f}"
            cv2.putText(frame, label_text, (x, y - 5), font, 0.6, color, 2)
            detected_count += 1
    
    # Add detection count overlay
    cv2.putText(frame, f"Objects: {detected_count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    return frame

def generate_webcam_frames(confidence_threshold=0.5):
    """Generator function for webcam streaming"""
    global webcam_active
    
    # Use DirectShow backend on Windows for better compatibility
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not camera.isOpened():
        print("Error: Could not open webcam with DirectShow, trying default...")
        camera = cv2.VideoCapture(0)
        
    if not camera.isOpened():
        print("Error: Could not open webcam")
        return
    
    # Set camera properties for better performance
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 30)
    
    try:
        while webcam_active:
            success, frame = camera.read()
            if not success:
                break
            
            # Detect objects in frame
            frame = detect_objects_frame(frame, confidence_threshold)
            
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            
            frame_bytes = buffer.tobytes()
            
            # Yield frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    finally:
        camera.release()
        print("Webcam released")

@app.route('/webcam/start', methods=['POST'])
def start_webcam():
    """Start webcam detection"""
    global webcam_active
    
    with webcam_lock:
        if webcam_active:
            return jsonify({'error': 'Webcam already active'}), 400
        
        webcam_active = True
    
    return jsonify({'success': True, 'message': 'Webcam started'})

@app.route('/webcam/stop', methods=['POST'])
def stop_webcam():
    """Stop webcam detection"""
    global webcam_active
    
    with webcam_lock:
        webcam_active = False
    
    return jsonify({'success': True, 'message': 'Webcam stopped'})

@app.route('/webcam/feed')
def webcam_feed():
    """Video streaming route for webcam"""
    confidence = float(request.args.get('confidence', 0.5))
    
    return Response(generate_webcam_frames(confidence),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/webcam/status')
def webcam_status():
    """Get webcam status"""
    return jsonify({'active': webcam_active})


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Real-time Object Identification using YOLO Algorithm")
    print("="*60)
    print("Server starting on http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
