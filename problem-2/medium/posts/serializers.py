from rest_framework import serializers

from posts import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            "id",
            "title",
            "author",
            "address",
            "contents",
            "created_at",
            "url",
        ]
