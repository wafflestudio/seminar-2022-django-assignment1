from django.urls import path
from .views import *


urlpatterns = [
    path('v1/posts/', blog_list, name="post_list"),
    path('v1/posts/<int:pk>/', blog_detail, name='post_detail')
]
