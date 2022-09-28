from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(blank=True)
    # ForeignKey 선언이 적절하나, 이번 과제에서 사용 금지인 관계로 CharField 사용
    user = models.CharField(max_length=30, null=True)
    # ForeignKey 선언이 적절하나, 이번 과제에서 사용 금지인 관계로 EmailField 사용
    user_email = models.EmailField(null=True)
    published_time = models.DateTimeField(auto_now_add=True, null=True)
    read_time_min = models.IntegerField(null=True)
    likes = models.IntegerField(default=0)
    # Comment model 의 ForeignKey 로 연결되어야 하나, 이번 과제에서 테이블 하나만을 사용하므로 코멘트의 개수만을 저장하는 IntegerField 사용
    comments = models.IntegerField(default=0)