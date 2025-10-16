from django.urls import path
from app.views import admin_dashboard, upload_files
from .views import issue_fine, client_dashboard
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("upload/", upload_files, name="upload_files"),
    path("issue_fine/", issue_fine, name="issue_fine"),
    path("client_dashboard/", client_dashboard, name="client_dashboard"),
    path('payment/',views.payment,name='payment'),
    path('qr/', views.qr, name='qr_page'),
    path('blog/', views.blog, name='blog'),
    path('conta/', views.conta, name='conta'),
    path('suc/', views.suc, name='suc')
    
 
]

