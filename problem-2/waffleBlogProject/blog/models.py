from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())
    author_email = models.EmailField(blank=True)










