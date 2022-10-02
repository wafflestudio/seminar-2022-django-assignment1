from .models import Post
from rest_framework import serializers, viewsets


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'mainText', 'uploadDate', 'userName', 'userMail')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
