from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    time_to_read = serializers.ReadOnlyField()
    image = serializers.ImageField(use_url=True, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'owner', 'email', 'time_to_read', 'image']
