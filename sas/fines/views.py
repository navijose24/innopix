from django.shortcuts import render, redirect
from .models import Fine
from users.models import ClientUser


def issue_fine(request):
    if request.method == "POST":
        try:
            vehicle_number = request.POST["vehicle_number"]
            phone_number = request.POST["phone_number"]
            amount = request.POST["amount"]
            
            # Validate amount
            amount = float(amount)  # Convert to float to validate
            
            Fine.objects.create(
                vehicle_number=vehicle_number,
                phone_number=phone_number,
                amount=amount,
                issued_by=request.user,
            )
            print(f"Fine issued to {phone_number} for {amount}")  # Replace with SMS
            return redirect("admin_dashboard")
        except KeyError as e:
            return render(request, "app/templates/fines/issue_fine.html", {"error": f"Missing field: {str(e)}"})
        except ValueError:
            return render(request, "app/templates/fines/issue_fine.html", {"error": "Invalid amount"})

    return render(request, "app/templates/fines/issue_fine.html")


def client_dashboard(request):
    """Displays fines for the logged-in client."""
    client_phone = request.session.get("client_phone")
    if not client_phone:
        return redirect("client_login")  # Redirect if no phone is stored in session

    fines = Fine.objects.filter(phone_number=client_phone, status="unpaid")
    return render(request, "app/templates/fines/client_dashboard.html", {"fines": fines})

def payment(request):
    return render(request, "payment.html")
def qr(request):
    return render(request, "qr.html")

def blog(request):
    return render(request,"blog.html")

def conta(request):
    return render(request,"conta.html")

def suc(request):
    return render(request,"suc.html")