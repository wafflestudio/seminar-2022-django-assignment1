from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    owner_name = models.CharField(max_length=30)
    owner_email = models.EmailField()
    datetime_created = models.DateTimeField()
    claps = models.PositiveIntegerField()

