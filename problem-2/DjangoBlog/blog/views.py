from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer