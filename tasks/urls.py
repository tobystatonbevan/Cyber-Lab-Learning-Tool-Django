# projects/urls.py

from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.task_index, name="task_index"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
]