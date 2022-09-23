from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Problem-2 ViewSet을 이용해 API 만들기
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


