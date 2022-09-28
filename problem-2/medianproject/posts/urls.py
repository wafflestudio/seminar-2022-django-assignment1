from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post")

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls)
]

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})