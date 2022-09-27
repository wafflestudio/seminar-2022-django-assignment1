from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
