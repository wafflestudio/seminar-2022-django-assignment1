from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

'''Problem-2 ViewSet을 이용해 API 만들기'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''Problem-3 Function Based View로 똑같은 역할의 API 만들기'''
# /v2/
@api_view(['GET'])
def api_root(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
# /v2/posts
@api_view(['GET', 'POST'])
def post_list(request):
    # GET 요청시 list posts
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    # POST 요청시 create post
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /v2/posts/<int:pk>
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    # pk값이 일치하는 post 가져오기
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET 요청시 detail a post
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # POST 요청시 update a post
    elif request.method == 'POST':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH 요청시 partial update a post
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DElETE 요청시 delete a post
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)