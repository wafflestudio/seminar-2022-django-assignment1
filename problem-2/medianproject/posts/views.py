from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


