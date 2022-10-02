from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=1000)
    description = models.TextField()