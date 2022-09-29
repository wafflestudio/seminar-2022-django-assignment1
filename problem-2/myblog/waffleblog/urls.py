from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.ArticleViewSet, basename='article')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/', views.article_list),
    path('v1/posts/<int:pk>/', views.article_detail),
]