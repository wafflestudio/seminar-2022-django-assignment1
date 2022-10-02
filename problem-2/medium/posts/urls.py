from django import urls
from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")

urlpatterns = [
    urls.path("v1/", urls.include(router.urls)),
    urls.path("v2/posts/", views.post_list, name="create_post"),
    urls.path("v2/posts/<int:pk>/", views.post_detail, name="create_post"),
]
