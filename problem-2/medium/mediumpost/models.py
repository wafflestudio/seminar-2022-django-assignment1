from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    mainText = models.TextField(max_length=200)
    uploadDate = models.DateTimeField(auto_now_add=True)
    userName = models.CharField(max_length=200, default='')
    userMail = models.EmailField(max_length=254)

    def __str__(self): return self.title
