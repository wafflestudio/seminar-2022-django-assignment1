from django.db import models


class Post(models.Model):
    created = models.DateTimeField('CREATED DATETIME', auto_now_add=True)
    modified = models.DateTimeField('MODIFIED DATETIME', auto_now=True)
    title = models.CharField('TITLE', max_length=100)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='description for your post')
    content = models.TextField('CONTENT', max_length=5000)
    owner = models.CharField('OWNER', max_length=50)
    email = models.EmailField('EMAIL')
    time_to_read = models.IntegerField('TIME', default=0)
    image = models.ImageField('IMAGE', upload_to='photos/%Y/%m/%d', null=True)

    class Meta:
        db_table = 'blog_posts'
        ordering = ['-modified']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.time_to_read = len(self.content) // 500 + 2
        super().save(*args, **kwargs)
