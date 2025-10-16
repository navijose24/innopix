
# Smart Automated System (SAS) : AI-Powered Waste Management system

A Django-based web application that uses computer vision and machine learning to detect traffic violations, focusing on vehicle detection, number plate recognition, and automated fine management.

## 🚀 Overview

The **Smart Automated System (SAS)** leverages **YOLO (You Only Look Once)** object detection to identify vehicles, detect number plates, and automatically issue fines for traffic violations. It supports both image and video inputs, enabling real-time monitoring.

## ✨ Features

### 🚗 Vehicle Detection

* Detects multiple vehicle types (cars, scooters, auto-rickshaws)
* Real-time image and video processing
* Integrated YOLO-based detection models

### 🏷️ Number Plate Recognition

* Automatically detects and maps number plates
* Uses a predefined database for vehicle-owner mapping
* Displays visual annotations on detected plates

### 💰 Fine Management

* Auto-generates fines for detected violations
* Tracks fine history and payment status
* Sends notifications to vehicle owners

### 🎨 Modern Web Interface

* Responsive and user-friendly design
* Separate dashboards for admin and users
* Easy drag-and-drop file upload

## ⚙️ Installation

### Prerequisites

* Python 3.8+
* FFmpeg (for video processing)
* Git

### Setup Steps

```bash
# Clone repository
git clone <repository-url>
cd sas

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows)
# or
source venv/bin/activate  # (macOS/Linux)

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

### FFmpeg Installation

* **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) → Add to PATH
* **macOS**: `brew install ffmpeg`
* **Linux**: `sudo apt install ffmpeg`

## 💻 Usage

### Uploading Files

1. Go to the upload page
2. Choose an image or video file
3. Click “Upload and Process”
4. View detection results

### Managing Fines

* **Admins:** View and issue fines, manage users, monitor data
* **Users:** Log in to view and pay fines

## 🧠 Model Configuration

Pre-trained YOLO models are used for object and number plate detection.
Update their paths in `fines/detection.py` if you move the models.

## 📁 Project Structure

```
sas/
├── sas/              # Django project
├── app/              # Core app (templates, static files)
├── fines/            # Fine and detection logic
├── users/            # Authentication & user management
├── media/            # Uploaded files
├── requirements.txt
└── README.md
```

## ⚡ Troubleshooting

* **FFmpeg Not Found** → Add to system PATH
* **Model Loading Error** → Check file paths and names
* **Database Issues** → Run migrations again: `python manage.py migrate`

## Acknowledgments

- YOLO team for the object detection framework
- Django community for the web framework
- OpenCV contributors for computer vision tools
- All contributors and testers

---

**Note:** This system is for educational and research purposes. Ensure compliance with local laws when applying automated monitoring systems.
