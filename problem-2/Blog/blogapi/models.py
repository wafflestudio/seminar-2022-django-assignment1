from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    author_mail = models.EmailField(max_length=100)
