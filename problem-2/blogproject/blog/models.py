from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
