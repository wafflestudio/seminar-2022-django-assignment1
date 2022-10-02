from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
from .views import get_post_list, get_post_detail_list

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', get_post_list),
    path('v2/posts/<int:pk>/', get_post_detail_list),
]