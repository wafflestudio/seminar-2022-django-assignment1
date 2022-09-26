from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', views.get_post_list, name="get_post_list"),
    path('v2/posts/<int:post_id>/', views.get_post_detail, name="get_post_detail"),
    path('v2/posts/<int:post_id>/', views.update_post, name="update_post"),
    path('v2/posts/<int:post_id>/', views.patch_post, name="patch_post"),
    path('v2/posts/<int:post_id>/', views.delete_post, name="delete_post"),
]
