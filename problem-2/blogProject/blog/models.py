from django.db import models

# 블로그 글
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date_time = models.DateTimeField()
    reading_time = models.IntegerField()
    image = models.ImageField()
    author_name = models.CharField(max_length=20)
    email_address = models.EmailField()
