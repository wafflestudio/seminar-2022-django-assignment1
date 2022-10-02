from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    authorimage = models.ImageField(upload_to='profile/', default='defaultprofile.png')
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100, default=False)
    body = models.TextField()
    bodyimage = models.ImageField(upload_to='body/', default='default.jpeg')
    published_date = models.DateTimeField()