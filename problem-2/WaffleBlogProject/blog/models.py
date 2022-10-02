from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(max_length=254, blank=True)
    author_image = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    reading_duration = models.DurationField(blank=True)

