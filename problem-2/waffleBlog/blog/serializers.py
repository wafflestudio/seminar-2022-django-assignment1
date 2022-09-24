from rest_framework import serializers
from blog.models import Post
from django.utils import timezone


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at', 'author', 'author_email']
