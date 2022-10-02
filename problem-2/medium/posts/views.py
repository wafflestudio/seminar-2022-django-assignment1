from django import http, shortcuts
from rest_framework import decorators, response, status, viewsets

from posts import models, serializers


# v1/posts/
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


# v2/posts/
@decorators.api_view(["GET", "POST"])
def post_list(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == "POST":
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return response.Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
        
    elif request.method == "GET":
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializer(instance=posts, many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@decorators.api_view(["PUT", "PATCH", "DELETE"])
def post_detail(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    if request.method == "DELETE":
        post = shortcuts.get_object_or_404(models.Post, pk=pk)
        post.delete()
        return http.HttpResponse(status=204)

    post = shortcuts.get_object_or_404(models.Post, pk=pk)
    if request.method == "PUT":
        serializer = serializers.PostSerializer(instance=post, data=request.data)
    elif request.method == "PATCH":
        serializer = serializers.PostSerializer(
            instance=post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
