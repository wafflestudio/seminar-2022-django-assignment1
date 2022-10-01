from rest_framework import viewsets

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
