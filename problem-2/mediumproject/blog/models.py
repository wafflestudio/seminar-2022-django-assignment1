from django.db import models

from datetime import date

# Create your models here.


class Post(models.Model):
    published = models.CharField(max_length=20, blank=True)
    author_name = models.CharField(max_length=20, default='')
    author_email = models.EmailField(default='')
    title = models.CharField(max_length=100, default='')
    posted_date = models.DateField()
    description = models.TextField()
    description_image = models.ImageField(blank=True)
    claps_count = models.IntegerField(default=0)
    response_count = models.IntegerField(default=0)
