from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64, blank=False)
    author_email = models.EmailField(max_length=128)


