from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', views.post_list),
    path('v2/posts/<int:pk>/', views.post_detail),
    path('admin/', admin.site.urls),
]

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})