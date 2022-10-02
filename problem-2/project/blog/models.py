from django.db import models


# Create your models here.
class Post(models.Model):
    writer = models.CharField(max_length=15, null=False)
    writer_email = models.EmailField(max_length=100)
    claps = models.IntegerField(default=0)

    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)

    written_time = models.DateTimeField(auto_now_add=True)
    reading_time = models.IntegerField(default=1) #대부분 분 단위의 reading time을 가지고 있음

    class Meta:
        ordering = ['written_time']