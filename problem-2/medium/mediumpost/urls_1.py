from django.urls import path, include
from mediumpost import views_1
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views_1.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]