from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# from blog.views import PostViewSet

# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# post_detail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

app_name = 'blog'
urlpatterns = [
    # path('posts/', post_list, name='list'),
    # path('posts/<int:pk>/', post_detail, name='detail'),
    path('v1/', include(router.urls)),
    path('v2/posts/', views.get_post_list),
    path('v2/posts/<int:pk>/', views.get_post_detail)
]
