from django.urls import path
from blog.views import PostViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = 'blog'
urlpatterns = [
    path('posts/', post_list, name='list'),
    path('posts/<int:pk>/', post_detail, name='detail')
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
