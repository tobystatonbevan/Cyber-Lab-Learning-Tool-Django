from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    technology = models.CharField(max_length=140)
    image = models.FileField(upload_to="task_images/",blank=True)
    