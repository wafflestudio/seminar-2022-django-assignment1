from django.urls import path
from . import views
# from views import PostViewset
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'posts', views.PostViewset)

urlpatterns = [
    # path('', include(router.urls),
    path("", views.post_list, name='post_list'),
    path("<int:pk>/", views.post_detail, name='post_detail'),
]