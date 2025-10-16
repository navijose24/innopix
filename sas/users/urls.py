from django.urls import path
from .views import admin_login, client_login, admin_dashboard, admin_logout

urlpatterns = [
    path("admin_login/", admin_login, name="admin_login"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("client_login/", client_login, name="client_login"),
    path("admin_logout/", admin_logout, name="admin_logout"),
]
