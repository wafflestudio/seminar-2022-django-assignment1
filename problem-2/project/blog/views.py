from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


"""
class-based viewsets
"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all posts, or create a new post.
    """
    posts = Post.objects.all()
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
## else: @api_view decorate에 의해 정해지지 않은 동작의 경우 405 Response 반환


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update, partial update or delete a post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)