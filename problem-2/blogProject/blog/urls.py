from django.urls import path
from . import views

urlpatterns=[
    path('v1/posts', views.PostView.as_view(), name=''),
    path('v1/posts/<int:pk>', views.DetailView.as_view(), name='')
]