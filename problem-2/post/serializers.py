from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'email', 'authorimage', 'title', 'subheading', 'body', 'bodyimage', 'published_date')