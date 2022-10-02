from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, default="")
    date = models.DateTimeField('date published', default=timezone.now)
    discription = models.TextField()
    email = models.EmailField(max_length=128, null=True)
    claps = models.IntegerField(default=0)
