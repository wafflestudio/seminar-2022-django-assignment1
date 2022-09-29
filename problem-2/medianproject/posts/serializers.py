from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'post_id', 'pub_date', 'title', 'publisher_name', 'publisher_email', 'text', 'file']