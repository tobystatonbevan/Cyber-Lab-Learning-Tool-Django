# lessons/urls.py

from django.urls import path
from lessons import views

urlpatterns = [
    path("", views.lesson_index, name="lesson_index"),
]