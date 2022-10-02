from django.db import models
from django import forms
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=127)
    writer = models.CharField(max_length=127, default='Unknown')
    description = models.TextField()
    email = models.EmailField(default='undefined@email.com')
    publish_time = models.DateTimeField(default=now)


