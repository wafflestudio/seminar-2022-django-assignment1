from django.urls import path
from posts import views2
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views2.api_root),
    path('posts/', views2.post_list, name='list'),
    path('posts/<int:pk>/', views2.post_detail, name='detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)
