from django.urls import path
from .apiviews import PostList, PostDetail


urlpatterns = [
    path('v1/posts/', PostList.as_view(), name="post_list"),
    path('v1/posts/<int:id>/', PostDetail.as_view(), name='post_detail')
]
