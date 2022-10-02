from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from v1.models import Post
from v1.serializers import PostSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, id):
    try:
        queryset = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = PostSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
