from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from blog.models import Post
# from blog.serializers import

# Create your views here.
class PostView(viewsets.ModelViewSet):
    pass

class DetailView(viewsets.ModelViewSet):
    pass
