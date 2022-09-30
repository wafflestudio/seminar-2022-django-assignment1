from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from json import loads, dumps

from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.core import serializers

# Create your views here.


def blog_list(request):
    if request.method == 'GET':  # 작동함
        post = Post.objects.all()
        data = serializers.serialize('json', post)
        return JsonResponse(data, status=200, safe=False)

    if request.method == 'POST':  # 작동함
        data = loads(request.body)
        post = Post.objects.create(
            date=timezone.now(),
            title=data['title'],  # .get('title'),
            link=data['link'],
            description=data['description'],
            tags=data['tags'],
            author_email=data['author_email'],
            content_format=data['content_format'],
            content=data['content'],
            canonical_url=data['canonical_url'],
            public_status=data['public_status'],
            notify_followers=data['notify_followers']

        )
        post.save()
        return HttpResponse(status=201)


def blog_detail(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        print(post)
        print(type(post))
        post_json = dict()
        post_json['title'] = post.title
        post_json['link'] = post.link
        post_json['description'] = post.description
        post_json['tags'] = post.tags
        post_json['author_email'] = post.author_email
        post_json['content_format'] = post.content_format
        post_json['content'] = post.content
        post_json['canonical_url'] = post.canonical_url
        post_json['public_status'] = post.public_status
        post_json['notify_followers'] = post.notify_followers
        return JsonResponse(post_json, status=200, safe=False)

    if request.method == 'PATCH':
        post = get_object_or_404(Post, pk=pk)
        data = request.body
        my_data = data.decode('utf8').replace("'", '"')
        my_data = loads(my_data)

        if 'title' in my_data:
            post.title = my_data['title']
        if 'link' in my_data:
            post.link = my_data['link']
        if 'description' in my_data:
            post.description = my_data['description']
        if 'tags' in my_data:
            post.tags = my_data['tags']
        if 'author_email' in my_data:
            post.author_email = my_data['author_email']
        if 'content_format' in my_data:
            post.content_format = my_data['content_format']
        if 'content' in my_data:
            post.content = my_data['content']
        if 'canonical_url' in my_data:
            post.canonical_url = my_data['canonical_url']
        if 'public_status' in my_data:
            post.public_status = my_data['public_status']
        if 'notify_followers' in my_data:
            post.notify_followers = my_data['notify_followers']
        post.save()

        return HttpResponse(status=200)

    if request.method == 'PUT':  # 작동함
        post = get_object_or_404(Post, pk=pk)
        data = loads(request.body)
        post.title = data['title']
        post.link = data['link']
        post.description = data['description']
        post.tags = data['tags']
        post.author_email = data['author_email']
        post.content_format = data['content_format']
        post.content = data['content']
        post.canonical_url = data['canonical_url']
        post.public_status = data['public_status']
        post.notify_followers = data['notify_followers']
        post.save()

        return HttpResponse(status=200)

    if request.method == 'DELETE':  # 작동함
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return HttpResponse(status=200)
