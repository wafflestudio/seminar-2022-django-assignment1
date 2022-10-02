from django.urls import path
from mediumpost import views_2

urlpatterns = [
    path('posts/', views_2.post_list),
    path('posts/<int:pk>/', views_2.post_detail),
]