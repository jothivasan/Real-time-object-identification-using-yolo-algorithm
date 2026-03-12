// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const confidenceSlider = document.getElementById('confidenceSlider');
const confidenceValue = document.getElementById('confidenceValue');
const processBtn = document.getElementById('processBtn');
const uploadSection = document.getElementById('uploadSection');
const processingSection = document.getElementById('processingSection');
const resultsSection = document.getElementById('resultsSection');
const processingStatus = document.getElementById('processingStatus');
const newDetectionBtn = document.getElementById('newDetectionBtn');
const originalMedia = document.getElementById('originalMedia');
const detectedMedia = document.getElementById('detectedMedia');
const detectedObjectsList = document.getElementById('detectedObjectsList');
const statsContent = document.getElementById('statsContent');
const downloadBtn = document.getElementById('downloadBtn');
const toast = document.getElementById('toast');

// Webcam Elements
const modeTabs = document.querySelectorAll('.mode-tab');
const webcamSection = document.getElementById('webcamSection');
const webcamFeed = document.getElementById('webcamFeed');
const webcamPlaceholder = document.getElementById('webcamPlaceholder');
const startWebcamBtn = document.getElementById('startWebcamBtn');
const stopWebcamBtn = document.getElementById('stopWebcamBtn');
const webcamConfidenceSlider = document.getElementById('webcamConfidenceSlider');
const webcamConfidenceValue = document.getElementById('webcamConfidenceValue');

let selectedFile = null;
let outputFilename = null;
let webcamActive = false;

// Confidence Slider
confidenceSlider.addEventListener('input', (e) => {
    const value = e.target.value;
    confidenceValue.textContent = `${value}%`;
});

// Upload Area - Click
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

// Upload Area - Drag and Drop
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileSelect(files[0]);
    }
});

// File Input Change
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFileSelect(e.target.files[0]);
    }
});

// Handle File Selection
function handleFileSelect(file) {
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'video/mp4', 'video/avi', 'video/mov', 'video/x-matroska'];
    const maxSize = 100 * 1024 * 1024; // 100MB
    
    if (!allowedTypes.includes(file.type)) {
        showToast('Invalid file type. Please upload an image or video.', 'error');
        return;
    }
    
    if (file.size > maxSize) {
        showToast('File too large. Maximum size is 100MB.', 'error');
        return;
    }
    
    selectedFile = file;
    
    // Update upload area
    const fileType = file.type.startsWith('image') ? 'Image' : 'Video';
    const fileSize = (file.size / (1024 * 1024)).toFixed(2);
    
    uploadArea.innerHTML = `
        <div class="upload-icon" style="color: var(--success);">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
        </div>
        <h3 style="color: var(--success);">File Selected!</h3>
        <p><strong>${file.name}</strong></p>
        <p>${fileType} • ${fileSize} MB</p>
        <p style="margin-top: 1rem; color: var(--text-muted); font-size: 0.875rem;">Click to choose a different file</p>
    `;
    
    processBtn.disabled = false;
    showToast(`${fileType} selected successfully!`, 'success');
}

// Process Button
processBtn.addEventListener('click', async () => {
    if (!selectedFile) {
        showToast('Please select a file first.', 'error');
        return;
    }
    
    // Show processing section
    uploadSection.classList.add('hidden');
    processingSection.classList.remove('hidden');
    
    const fileType = selectedFile.type.startsWith('image') ? 'image' : 'video';
    processingStatus.textContent = `Analyzing your ${fileType} with YOLO neural network...`;
    
    // Prepare form data
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('confidence', confidenceSlider.value / 100);
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            displayResults(result);
        } else {
            throw new Error(result.error || 'Processing failed');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Processing failed: ' + error.message, 'error');
        resetToUpload();
    }
});

// Display Results
function displayResults(result) {
    processingSection.classList.add('hidden');
    resultsSection.classList.remove('hidden');
    
    const isVideo = result.file_type === 'video';
    outputFilename = result.output_file;
    
    // Display original media
    if (isVideo) {
        originalMedia.innerHTML = `
            <video controls>
                <source src="/uploads/${result.input_file}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        `;
    } else {
        originalMedia.innerHTML = `
            <img src="/uploads/${result.input_file}" alt="Original">
        `;
    }
    
    // Display detected media
    if (isVideo) {
        detectedMedia.innerHTML = `
            <video controls autoplay loop>
                <source src="/outputs/${result.output_file}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        `;
    } else {
        detectedMedia.innerHTML = `
            <img src="/outputs/${result.output_file}" alt="Detected">
        `;
    }
    
    // Display detected objects
    if (isVideo) {
        // For videos, show unique objects detected
        detectedObjectsList.innerHTML = result.result.detected_objects.map(obj => `
            <div class="object-tag">
                <span>${obj}</span>
            </div>
        `).join('');
        
        // Display video stats
        statsContent.innerHTML = `
            <div class="stat-row">
                <span>Unique Objects</span>
                <span>${result.result.detected_objects.length}</span>
            </div>
            <div class="stat-row">
                <span>Total Frames</span>
                <span>${result.result.total_frames}</span>
            </div>
            <div class="stat-row">
                <span>Duration</span>
                <span>${result.result.duration}</span>
            </div>
            <div class="stat-row">
                <span>File Type</span>
                <span>Video</span>
            </div>
        `;
    } else {
        // For images, show objects with confidence
        detectedObjectsList.innerHTML = result.result.detected_objects.map(obj => `
            <div class="object-tag">
                <span>${obj.label}</span>
                <span class="object-confidence">${obj.confidence}</span>
            </div>
        `).join('');
        
        // Display image stats
        statsContent.innerHTML = `
            <div class="stat-row">
                <span>Total Detections</span>
                <span>${result.result.total_detections}</span>
            </div>
            <div class="stat-row">
                <span>Confidence Threshold</span>
                <span>${confidenceSlider.value}%</span>
            </div>
            <div class="stat-row">
                <span>File Type</span>
                <span>Image</span>
            </div>
        `;
    }
    
    showToast('Detection completed successfully!', 'success');
}

// Download Button
downloadBtn.addEventListener('click', () => {
    if (outputFilename) {
        window.location.href = `/outputs/${outputFilename}`;
        showToast('Download started!', 'success');
    }
});

// New Detection Button
newDetectionBtn.addEventListener('click', () => {
    resetToUpload();
});

// Reset to Upload
function resetToUpload() {
    resultsSection.classList.add('hidden');
    processingSection.classList.add('hidden');
    uploadSection.classList.remove('hidden');
    
    // Reset upload area
    uploadArea.innerHTML = `
        <div class="upload-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="17 8 12 3 7 8"/>
                <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
        </div>
        <h3>Drop your file here or click to browse</h3>
        <p>Supports: JPG, PNG, GIF, MP4, AVI, MOV (Max 100MB)</p>
    `;
    
    selectedFile = null;
    outputFilename = null;
    fileInput.value = '';
    processBtn.disabled = true;
    confidenceSlider.value = 50;
    confidenceValue.textContent = '50%';
}

// Toast Notification
function showToast(message, type = 'success') {
    const toastMessage = toast.querySelector('.toast-message');
    toastMessage.textContent = message;
    
    toast.className = `toast ${type}`;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Prevent default drag behavior on document
document.addEventListener('dragover', (e) => {
    e.preventDefault();
});

document.addEventListener('drop', (e) => {
    e.preventDefault();
});

// Add smooth scroll behavior
document.documentElement.style.scrollBehavior = 'smooth';

// ===== WEBCAM FUNCTIONALITY =====

// Mode Switching
modeTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const mode = tab.dataset.mode;
        
        // Update active tab
        modeTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        // Show/hide sections
        if (mode === 'upload') {
            uploadSection.classList.remove('hidden');
            webcamSection.classList.add('hidden');
            if (webcamActive) {
                stopWebcam();
            }
        } else if (mode === 'webcam') {
            uploadSection.classList.add('hidden');
            webcamSection.classList.remove('hidden');
            resultsSection.classList.add('hidden');
            processingSection.classList.add('hidden');
        }
    });
});

// Webcam Confidence Slider
webcamConfidenceSlider.addEventListener('input', (e) => {
    const value = e.target.value;
    webcamConfidenceValue.textContent = `${value}%`;
    
    // Update feed if webcam is active
    if (webcamActive) {
        const confidence = value / 100;
        webcamFeed.src = `/webcam/feed?confidence=${confidence}&t=${Date.now()}`;
    }
});

// Start Webcam
startWebcamBtn.addEventListener('click', async () => {
    try {
        startWebcamBtn.disabled = true;
        
        const response = await fetch('/webcam/start', {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.success) {
            webcamActive = true;
            
            // Update UI
            webcamPlaceholder.classList.add('hidden');
            webcamFeed.classList.remove('hidden');
            startWebcamBtn.classList.add('hidden');
            stopWebcamBtn.classList.remove('hidden');
            
            // Start video feed
            const confidence = webcamConfidenceSlider.value / 100;
            webcamFeed.src = `/webcam/feed?confidence=${confidence}`;
            
            showToast('Webcam started successfully!', 'success');
        } else {
            throw new Error(result.error || 'Failed to start webcam');
        }
    } catch (error) {
        console.error('Error starting webcam:', error);
        showToast('Failed to start webcam: ' + error.message, 'error');
        startWebcamBtn.disabled = false;
    }
});

// Stop Webcam
stopWebcamBtn.addEventListener('click', async () => {
    await stopWebcam();
});

async function stopWebcam() {
    try {
        const response = await fetch('/webcam/stop', {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.success) {
            webcamActive = false;
            
            // Update UI
            webcamFeed.src = '';
            webcamFeed.classList.add('hidden');
            webcamPlaceholder.classList.remove('hidden');
            stopWebcamBtn.classList.add('hidden');
            startWebcamBtn.classList.remove('hidden');
            startWebcamBtn.disabled = false;
            
            showToast('Webcam stopped', 'success');
        }
    } catch (error) {
        console.error('Error stopping webcam:', error);
        showToast('Failed to stop webcam: ' + error.message, 'error');
    }
}

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (webcamActive) {
        fetch('/webcam/stop', { method: 'POST' });
    }
});

console.log('Real-time Object Identification using YOLO - Ready!');
