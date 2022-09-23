from django.db import models

# 블로그 글(post) 모델
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    reading_time = models.IntegerField()
    image = models.ImageField()
    author_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    claps = models.IntegerField()
