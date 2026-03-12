import cv2
import sys

print("Testing camera access...")
print(f"OpenCV version: {cv2.__version__}")

# Try to open camera
print("\nAttempting to open camera 0...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ ERROR: Could not open camera 0")
    print("\nTrying camera 1...")
    cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("❌ ERROR: Could not open camera 1 either")
        print("\nPossible reasons:")
        print("1. No webcam is connected")
        print("2. Another application is using the camera")
        print("3. Camera permissions are denied")
        print("4. Camera drivers are not installed")
        sys.exit(1)
    else:
        print("✅ SUCCESS: Camera 1 is working!")
        camera_index = 1
else:
    print("✅ SUCCESS: Camera 0 is working!")
    camera_index = 0

# Get camera properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"\nCamera {camera_index} properties:")
print(f"  Resolution: {int(width)}x{int(height)}")
print(f"  FPS: {fps}")

# Try to read a frame
print("\nAttempting to read a frame...")
ret, frame = cap.read()

if ret:
    print("✅ SUCCESS: Frame captured successfully!")
    print(f"  Frame shape: {frame.shape}")
else:
    print("❌ ERROR: Could not read frame from camera")

cap.release()
print("\n✅ Camera test completed!")
print(f"\nRECOMMENDATION: Use camera index {camera_index} in your app.py")
