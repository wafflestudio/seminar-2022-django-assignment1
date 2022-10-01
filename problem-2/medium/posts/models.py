from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    address = models.EmailField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True)
