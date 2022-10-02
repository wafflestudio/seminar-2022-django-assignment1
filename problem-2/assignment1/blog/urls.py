from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, post_list, post_detail

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post")

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', post_list),
    path('v2/posts/<int:pk>', post_detail)
]



