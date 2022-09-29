from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer, PostSerializerForFBV

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializerForFBV(post, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializerForFBV(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializerForFBV(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializerForFBV(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = PostSerializerForFBV(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)