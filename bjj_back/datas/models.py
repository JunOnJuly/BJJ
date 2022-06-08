from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField(unique=True)
    thumbnail = models.TextField()
    description = models.TextField()
    channel = models.TextField()
    black = models.BooleanField(default=0)