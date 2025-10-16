import cv2
import numpy as np
from ultralytics import YOLO
import os
import subprocess
import uuid  # To generate unique filenames

# Class names mapping
class_names = {
    0: "auto",
    1: "car",
    2: "hand",
    3: "number plate",
    4: "scooter",
    5: "waste",
}

# Assign colors
colors = {
    0: (255, 165, 0),  # Auto - Orange
    1: (0, 255, 0),  # Car - Green
    2: (255, 0, 0),  # Hand - Blue
    3: (0, 0, 255),  # Number Plate - Red
    4: (255, 255, 0),  # Scooter - Yellow
    5: (0, 0, 255),  # Waste - Red
}

# Predefined number plates for detected vehicles
predefined_plates = {
    "auto": "KL06 G7092",
    "car": "KL05 AG 4446",
    "scooter": "KL35 K 8975"
}

def convert_video(input_path, output_path):
    """
    Converts the processed video to MP4 using FFmpeg.
    """
    command = [
        "ffmpeg", "-i", input_path,
       
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-strict", "experimental",
        output_path
    ]
    try:
        subprocess.run(command, check=True)
        print(f"✅ Video converted successfully: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg Error: {e}")

def detect_objects(input_file, is_video):
    """
    Detect objects in an image or video using YOLO and return the processed file.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, "app", "templates", "fintun final nav part2.pt")
    model = YOLO(model_path)
    
    detected_plates = []
    processed_video_path = None

    if not is_video:
        image = cv2.imread(input_file)
        if image is None:
            print(f"Error: Unable to read image {input_file}")
            return None, []
        results = model(image)
        for r in results:
            for box in r.boxes:
                class_id = int(box.cls[0])
                label = class_names.get(class_id, "Unknown")
                plate_text = predefined_plates.get(label, "N/A")
                detected_plates.append(f"{label}, Plate:{plate_text}")
                print(f"Detected in Image: {label}, Plate: {plate_text}")
        return None, detected_plates  

    else:
        cap = cv2.VideoCapture(input_file)
        if not cap.isOpened():
            print(f"Error: Unable to read video {input_file}")
            return None, []

        unique_id = uuid.uuid4().hex[:6]  # Generate a short unique ID
        processed_video_filename = f"processed_{unique_id}.avi"
        converted_video_filename = f"converted_{unique_id}.mp4"

        processed_video_path = os.path.join(BASE_DIR, "media","uploads" ,"processed_videos", processed_video_filename)
        converted_video_path = os.path.join(BASE_DIR, "media","uploads", "processed_videos", converted_video_filename)
        #convert_video(processed_video_path,converted_video_path,width=1800,height=180)

        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(processed_video_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            for r in results:
                for box in r.boxes:
                    class_id = int(box.cls[0])
                    label = class_names.get(class_id, "Unknown")
                    plate_text = predefined_plates.get(label, "N/A")
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Choose color
                    color = colors.get(class_id, (0, 255, 255))  # Default: Cyan

                    # Draw rectangle
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                    # Display label
                    text = f"{label}: {plate_text}"
                    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    detected_plates.append(f"{label}, Plate: {plate_text}")
            out.write(frame)

        cap.release()
        out.release()

        print(f"✅ Processed video saved at: {processed_video_path}")

        # Convert to MP4 format using FFmpeg
        convert_video(processed_video_path, converted_video_path)

        return converted_video_path, detected_plates