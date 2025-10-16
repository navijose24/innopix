import cv2
import numpy as np
from ultralytics import YOLO
import os
import subprocess
import uuid
from dotenv import load_dotenv  # <-- NEW

# Load environment variables
load_dotenv()

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
    0: (255, 165, 0),
    1: (0, 255, 0),
    2: (255, 0, 0),
    3: (0, 0, 255),
    4: (255, 255, 0),
    5: (0, 0, 255),
}


pred_plates = {
    "auto": os.getenv("AUTO_PLATE"),
    "car": os.getenv("CAR_PLATE"),
    "scooter": os.getenv("SCOOTER_PLATE")
}

def convert_video(input_path, output_path):
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
                plate_text = pred_plates.get(label, "N/A")
                detected_plates.append(f"{label}, Plate:{plate_text}")
                print(f"Detected in Image: {label}, Plate: {plate_text}")
        return None, detected_plates  

    else:
        cap = cv2.VideoCapture(input_file)
        if not cap.isOpened():
            print(f"Error: Unable to read video {input_file}")
            return None, []

        unique_id = uuid.uuid4().hex[:6]
        processed_video_filename = f"processed_{unique_id}.avi"
        converted_video_filename = f"converted_{unique_id}.mp4"

        processed_video_path = os.path.join(BASE_DIR, "media", "processed_videos", processed_video_filename)
        converted_video_path = os.path.join(BASE_DIR, "media", "processed_videos", converted_video_filename)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
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
                    plate_text = pred_plates.get(label, "N/A")

                    # Mask for display only
                    display_plate = ''.join('*' if c.isalnum() else c for c in plate_text)

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    color = colors.get(class_id, (0, 255, 255))

                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    text = f"{label}: {display_plate}"
                    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                    detected_plates.append(f"{label}, Plate: {plate_text}")

            out.write(frame)

        cap.release()
        out.release()

        print(f"✅ Processed video saved at: {processed_video_path}")
        convert_video(processed_video_path, converted_video_path)

        return converted_video_path, detected_plates