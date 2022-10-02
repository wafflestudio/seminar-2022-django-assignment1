from rest_framework import serializers
from v1.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'date', 'email', 'description']