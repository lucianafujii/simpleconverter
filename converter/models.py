from django.db import models

class VideoFile(models.Model):
    filename = models.CharField(max_length=120)
    media_id = models.PositiveIntegerField(default=0)
    ready = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
