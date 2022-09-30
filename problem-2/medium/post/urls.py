from django.urls import include, path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', views.posts_list, name="post_list"),
    path('v2/posts/<int:pk>', views.post_detail, name="post_detail")
]
