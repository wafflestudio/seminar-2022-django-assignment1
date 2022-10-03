from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'v1/posts', views.PostViewSet, basename="post")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('v2/posts', views.post_list),
    path('v2/posts/<int:pk>', views.post_detail)
]
