from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.settings import api_settings

from blog.models import Post
from blog.serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(('GET', 'POST'))
def get_post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            headers = {'Location': str(serializer.data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            headers = {}
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
def get_post_detail(request, pk):
    instance = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(instance, many=False)
        return Response(serializer.data)

    if request.method in ['PATCH', 'PUT']:
        partial = (request.method == 'PATCH')
        serializer = PostSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)