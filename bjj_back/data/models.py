from django.db import models
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()

class VideoComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='videocomments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videocomments')
    content = models.CharField(max_length=100)