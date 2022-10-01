from django import urls
from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")

urlpatterns = [
    urls.path("v1/posts/", urls.include(router.urls)),
    urls.path("v2/posts/", views.get_all_posts, name="get_all_posts"),
    urls.path("v2/posts/", views.create_post, name="create_post"),
    urls.path("v2/posts/<int:pk>/", views.get_post_detail, name="get_post_detail"),
    urls.path("v2/posts/<int:pk>/", views.update_post, name="update_post"),
    urls.path("v2/posts/<int:pk>/", views.patch_post, name="patch_post"),
    urls.path("v2/posts/<int:pk>/", views.delete_post, name="delete_post"),
]
