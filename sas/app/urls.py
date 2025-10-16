# filepath: my_app/urls.py
from django.urls import path
from . import views
from .views import upload_files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.login, name="login"),
    path("home", views.home, name="home"),
    path("upload/", upload_files, name="upload_file"),
    
    #path("pay-fine/<str:number_plate>/", pay_fine, name="pay_fine")

]

 