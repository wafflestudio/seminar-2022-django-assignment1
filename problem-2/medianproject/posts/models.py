from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, max_length=200)
    publisher_name = models.CharField(null=False, max_length=50)
    publisher_email = models.EmailField(null=False)
    text = models.TextField(null=False)
    file = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ['pub_date']