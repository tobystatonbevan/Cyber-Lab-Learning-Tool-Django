from django.db import models

class Vulnerability(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
