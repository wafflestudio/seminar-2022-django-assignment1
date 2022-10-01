from django import http, shortcuts
from rest_framework import decorators, request, viewsets

from posts import models, serializers


# v1/posts/
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


# v2/posts/
@decorators.api_view(["GET"])
def get_all_posts(request: request.Request) -> http.HttpResponse:
    posts = models.Post.objects.all()
    serializer = serializers.PostSerializer(instance=posts, many=True)
    return http.JsonResponse(data=serializer.data, status=200)


@decorators.api_view(["POST"])
def create_post(request: request.Request) -> http.HttpResponse:
    serializer = serializers.PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return http.JsonResponse(data=serializer.data, status=200)
    return http.JsonResponse(data=serializer.errors, status=400)


@decorators.api_view(["GET"])
def get_post_detail(request: request.Request, pk: int) -> http.HttpResponse:
    post = shortcuts.get_object_or_404(models.Post, pk=pk)
    serializer = serializers.PostSerializer(instance=post)
    return http.JsonResponse(data=serializer.data, status=200)


@decorators.api_view(["PUT"])
def update_post(request: request.Request, pk: int) -> http.HttpResponse:
    post = shortcuts.get_object_or_404(models.Post, pk=pk)
    serializer = serializers.PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return http.JsonResponse(data=serializer.data, status=200)
    return http.JsonResponse(data=serializer.errors, status=400)


@decorators.api_view(["PATCH"])
def patch_post(request: request.Request, pk: int) -> http.HttpResponse:
    post = shortcuts.get_object_or_404(models.Post, pk=pk)
    serializer = serializers.PostSerializer(
        instance=post, data=request.data, partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return http.JsonResponse(data=serializer.data, status=200)
    return http.JsonResponse(data=serializer.errors, status=400)


@decorators.api_view(["DELETE"])
def delete_post(request: request.Request, pk: int) -> http.HttpResponse:
    post = shortcuts.get_object_or_404(models.Post, pk=pk)
    post.delete()
    return http.HttpResponse(status=204)
