from django.urls import path
from .apiviews import PostList, PostDetail


urlpatterns = [
    path('posts/', PostList.as_view(), name="post_list"),
    path('posts/<int:id>/', PostDetail.as_view(), name='post_detail')    
]
