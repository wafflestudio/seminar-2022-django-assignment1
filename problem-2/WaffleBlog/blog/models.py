from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100, default='admin')
    contents = models.TextField()
    read_time = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=100)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
