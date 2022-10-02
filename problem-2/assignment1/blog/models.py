from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=50, default='')
    contents = models.TextField()
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['created']
