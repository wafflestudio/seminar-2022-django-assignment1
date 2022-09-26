from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from blogapi.models import Post
from blogapi.serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
def get_post_list(request: Request):
    posts = Post.objects.all()

    if request.method == "POST":
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_post_detail(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_post(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_post(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request:Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
