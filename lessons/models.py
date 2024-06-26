from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    technology = models.CharField(max_length=140)
    image = models.FileField(upload_to="lesson_images/",blank=True)