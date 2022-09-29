from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "date",
            "link",
            "description",
            "tags",
            "author_email",
            "content_format",
            "content",
            "canonical_url",
            "public_status",
            "notify_followers"
        ]
