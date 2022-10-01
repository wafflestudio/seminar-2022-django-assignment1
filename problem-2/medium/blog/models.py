from django.db import models

# Create your models here.
class Post(models.Model):
    nickname = models.CharField(max_length=50, null='True')
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()