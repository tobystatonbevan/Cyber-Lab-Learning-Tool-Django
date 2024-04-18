from django.urls import path
from assignments import views

urlpatterns = [
    path("", views.assignment_index, name="assignment_index"),
    path("<int:pk>/", views.assignment_detail, name="assignment_detail"),
]