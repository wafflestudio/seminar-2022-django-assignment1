from django.db import models


# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    read_time = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']
