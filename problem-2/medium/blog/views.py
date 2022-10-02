
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(['GET','PUT','PATCH','DELETE'])
def post_detail(request,pk):
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.get(pk=pk))
    elif request.method == 'PUT':
        serializer = PostSerializer(Post.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
    elif request.method == 'PATCH':
        serializer = PostSerializer(Post.objects.get(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
    elif request.method == 'DELETE':
        Post.objects.get(pk=pk).delete()
    return Response(serializer.data)