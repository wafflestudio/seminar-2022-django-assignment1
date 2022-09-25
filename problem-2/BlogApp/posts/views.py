from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.validated_data['time_to_read'] = len(serializer.validated_data['content']) // 500 + 2
        serializer.save()

    def perform_update(self, serializer):
        serializer.validated_data['time_to_read'] = len(serializer.validated_data['content']) // 500 + 2
        serializer.save()

    def perform_destroy(self, instance):
        if instance.image:
            instance.image.delete()
        instance.delete()

# class PostList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetail(APIView):
#         """
#         Retrieve, update or delete a snippet instance.
#         """
#
#         def get_object(self, pk):
#             try:
#                 return Post.objects.get(pk=pk)
#             except Post.DoesNotExist:
#                 raise Http404
#
#         def get(self, request, pk, format=None):
#             post = self.get_object(pk)
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#
#         def put(self, request, pk, format=None):
#             post = self.get_object(pk)
#             serializer = PostSerializer(post, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         def delete(self, request, pk, format=None):
#             post = self.get_object(pk)
#             post.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)