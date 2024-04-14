# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("admin_details/", views.admin_details, name='admin_details'),
]