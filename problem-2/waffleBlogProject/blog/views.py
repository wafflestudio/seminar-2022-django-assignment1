from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from blog.models import Post
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from blog.serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(('GET','POST'))
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method=='POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET','PUT','PATCH','DELETE'))
def post_list_id(request, pk):
    if request.method == 'GET':
        post=get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


