from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, blank=True)
    author_photo = models.ImageField(upload_to='upload_photo/', default='default.jpg')
    article_photo = models.ImageField(upload_to='upload_image/', blank=True, null=True)
    author_email = models.EmailField(blank=True)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())
    reading_time = models.DurationField(blank=True, null=True)














