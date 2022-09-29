from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    pass


def get_list(request):
    pass


def get_detail(request, pk):
    pass


def put_detail(request, pk):
    pass


def patch_detail(request, pk):
    pass


def delete_detail(request, pk):
    pass


def blog_list(request):
    post = Post.objects.all()
    data = {
        "results": list(post.values(
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
        ))
    }
    return JsonResponse(data)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        "results": {
            "title": Post.title,
            "date": Post.date,
            "link": Post.link,
            "description": Post.description,
            "tags": Post.tags,
            "author_email": Post.author_email,
            "content_format": Post.content_format,
            "content": Post.content,
            "canonical_url": Post.canonical_url,
            "public_status": Post.public_status,
            "notify_followers": Post.notify_followers
        }
    }
    return JsonResponse(data)


def create_view(request):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, context)
