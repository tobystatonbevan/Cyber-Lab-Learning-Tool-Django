from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    technology = models.CharField(max_length=140)