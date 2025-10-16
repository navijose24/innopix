from django.shortcuts import render, redirect
from fines.detection import detect_objects
import os
from fines.models import VehicleOwner
from django.utils.timezone import now
from datetime import timedelta
from fines.utils import send_fine_notification


def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "homepage.html")


from django.conf import settings

def upload_files(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]
        file_path = os.path.join(settings.MEDIA_ROOT, "uploads", uploaded_file.name)

        # Ensure the upload directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save the uploaded file
        with open(file_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Detect number plates & process video
        is_video = uploaded_file.content_type.startswith("video")
        processed_video_path, detected_data = detect_objects(file_path, is_video)  
        print("Detect Objects Output:", detected_data)  # ✅ Debugging

        if not isinstance(detected_data, list):  
            raise ValueError("Unexpected return value from detect_objects")

        
        # Store processed video path in session
        if processed_video_path:
         processed_video_filename = os.path.basename(processed_video_path)
         request.session["processed_video"] = f"/media/uploads/processed_videos/{processed_video_filename}"

        # 🔹 Extract number plates
        detected_plates = [entry.split("Plate: ")[-1].strip() for entry in detected_data if "Plate:" in entry]
        print("Extracted Plates:", detected_plates)  # ✅ Debugging
        
        request.session["detected_plates"] = detected_plates
        request.session.modified = True  # Ensure session is saved

        # 🔹 Fetch vehicle owner details & send SMS
        owners = VehicleOwner.objects.filter(number_plate__in=detected_plates)
        print("Owners Retrieved:", list(owners))  # ✅ Debugging
        
        for owner in owners:
            fine_amount = 500  # Change as needed
            send_fine_notification(owner.phone_no, owner.number_plate, fine_amount)

        return redirect("admin_dashboard")

    return render(request, "fines/upload.html")


def admin_dashboard(request):
    detected_plates = request.session.get("detected_plates", [])
    print("Session Detected Plates in Dashboard:", detected_plates)  # ✅ Debugging
    
    # Fetch owners based on stored number plates
    owners = VehicleOwner.objects.filter(number_plate__in=detected_plates).values(
        "number_plate", "owner_name", "phone_no"
    )
    
    print("Owners Passed to Dashboard:", list(owners))  # ✅ Debugging

    return render(request, "users/admin_dashboard.html", {"owners": owners})



def home(request):
    detected_plates = request.session.get("detected_plates", [])
    print("home session called")
    owners = VehicleOwner.objects.filter(number_plate__in=detected_plates).values(
        "number_plate", "owner_name", "phone_no"
    )
    processed_video_path = request.session.get("processed_video")



    return render(
        request,
        "homepage.html",
        {
            
            "owners": owners,"processed_video": processed_video_path
        }
    )


from django.shortcuts import render

  # Ensure this template exists