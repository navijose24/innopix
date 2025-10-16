# Smart Automated System (SAS)

A Django-based web application that uses computer vision and machine learning to detect traffic violations, specifically focusing on vehicle detection, number plate recognition, and automated fine management.

## Project Overview

The Smart Automated System (SAS) is an intelligent traffic monitoring solution that leverages YOLO (You Only Look Once) object detection models to identify vehicles, detect number plates, and automatically issue fines for traffic violations. The system processes both images and videos to provide real-time monitoring capabilities.

## Features

### 🚗 Vehicle Detection
- **Multi-vehicle Support**: Detects cars, scooters, and auto-rickshaws
- **Real-time Processing**: Handles both image and video inputs
- **YOLO Integration**: Uses state-of-the-art object detection models

### 🏷️ Number Plate Recognition
- **Automatic Plate Detection**: Identifies number plates in detected vehicles
- **Predefined Plate Database**: Maps detected vehicles to known license plates
- **Visual Annotation**: Draws bounding boxes and labels on detected objects

### 📹 Video Processing
- **Video Upload Support**: Accepts MP4 video files for processing
- **Real-time Conversion**: Converts processed videos to MP4 format using FFmpeg
- **Frame-by-frame Analysis**: Processes each frame for object detection

### 💰 Fine Management System
- **Automated Fine Issuance**: Generates fines based on detected violations
- **User Management**: Separate interfaces for administrators and clients
- **Fine Tracking**: Tracks fine status and payment information
- **Notification System**: Sends notifications for issued fines

### 🎨 Modern Web Interface
- **Responsive Design**: Mobile-friendly interface
- **Admin Dashboard**: Comprehensive admin panel for system management
- **User Dashboard**: Client interface for viewing fines and payments
- **File Upload**: Easy drag-and-drop file upload functionality

## Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg (for video processing)
- Git

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended for video processing)
- **Storage**: At least 2GB free space
- **Graphics**: GPU support recommended for faster processing

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd sas
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**
   
   **Windows:**
   - Download from [FFmpeg official website](https://ffmpeg.org/download.html)
   - Add FFmpeg to your system PATH
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the Application

- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **User Dashboard**: http://127.0.0.1:8000/users/login/

### Uploading Files

1. Navigate to the upload page
2. Select an image or video file
3. Click "Upload and Process"
4. View the processed results with detected objects

### Managing Fines

1. **Admin Users**:
   - Access the admin dashboard
   - View all detected violations
   - Issue and manage fines
   - Monitor system statistics

2. **Client Users**:
   - Login to view personal fines
   - Check fine status and details
   - Access payment information

### Model Configuration

The system uses pre-trained YOLO models located in:
- `app/templates/fintun final nav part2.pt` - Main detection model
- `app/templates/littering_best.pt` - Littering detection model
- `app/templates/nimms best.pt` - Additional detection model

## Project Structure

```
sas/
├── sas/                    # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── app/                    # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── templates/         # HTML templates
│   └── static/            # Static files (CSS, JS, images)
├── fines/                 # Fine management app
│   ├── models.py          # Fine and vehicle models
│   ├── detection.py       # Object detection logic
│   └── views.py           # Fine-related views
├── users/                 # User management app
│   ├── models.py          # User models
│   └── views.py           # Authentication views
├── media/                 # Uploaded files
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Model Paths

Update model paths in `fines/detection.py` if you place models in different locations.

## Troubleshooting

### Common Issues

1. **FFmpeg Not Found**
   - Ensure FFmpeg is installed and added to system PATH
   - Restart your terminal/command prompt after installation

2. **Model Loading Errors**
   - Verify model files exist in the specified paths
   - Check file permissions

3. **Video Processing Issues**
   - Ensure sufficient disk space for temporary files
   - Check video format compatibility

4. **Database Errors**
   - Run migrations: `python manage.py migrate`
   - Check database file permissions

### Performance Optimization

- Use GPU acceleration for faster processing
- Increase system memory for large video files
- Consider using a production database (PostgreSQL) for better performance

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation for common solutions

## Acknowledgments

- YOLO team for the object detection framework
- Django community for the web framework
- OpenCV contributors for computer vision tools
- All contributors and testers

---

**Note**: This system is designed for educational and research purposes. Ensure compliance with local laws and regulations when implementing automated traffic monitoring systems.
