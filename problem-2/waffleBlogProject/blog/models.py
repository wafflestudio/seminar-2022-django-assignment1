from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    publisher_email = models.EmailField(max_length=200, blank=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title
