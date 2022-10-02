from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'v1', views.PostViewSet, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    path('v2/', views.post_list),
    path('v2/<int:id>/', views.post_detail),
]