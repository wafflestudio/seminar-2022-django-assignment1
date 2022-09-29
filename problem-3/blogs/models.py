from collections import UserString
from ctypes.wintypes import tagSIZE
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=200)
    description = models.TextField()
    tags = models.JSONField()
    author_email = models.EmailField()
    content_format = models.CharField(max_length=10)
    content = models.TextField()
    canonical_url = models.URLField(max_length=200)
    public_status = models.CharField(max_length=10)
    notify_followers = models.BooleanField()

    def __str__(self):
        return self.title
