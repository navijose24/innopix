from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import ClientUser
from django.contrib.auth import logout

def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("admin_dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/admin_login.html", {"form": form})


@login_required
def admin_dashboard(request):
    return render(request, "users/admin_dashboard.html")


def client_login(request):
    """Allows client login using only a phone number, without OTP verification."""
    if request.method == "POST":
        phone = request.POST["phone_number"]
        client, created = ClientUser.objects.get_or_create(phone_number=phone)
        request.session["client_phone"] = client.phone_number  # Store phone in session
        return redirect("client_dashboard")  # Redirect to client dashboard

    return render(request, "app/templates/users/client_login.html")


def admin_logout(request):
    logout(request)
    return redirect("admin_login")
