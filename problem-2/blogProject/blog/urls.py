from django.urls import path, include
from rest_framework import routers
from . import views

# Problem-2 ViewSet + Router을 이용해 API 만들기
router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns=[
    # Problem-2
    path('v1/', include(router.urls)),
    # Problem-3
    path('v2/', views.api_root),
    path('v2/posts/', views.post_list),
    path('v2/posts/<int:pk>', views.post_detail)
]