from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    reading_time = models.PositiveIntegerField(null=True, blank=True)
    author = models.CharField(max_length=50, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['created']
