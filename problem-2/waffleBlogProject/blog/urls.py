from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import post_list, post_list_id

router=DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/',post_list),
    path('v2/posts/<int:pk>/',post_list_id),
]