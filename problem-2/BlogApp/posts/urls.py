from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts import views
from django.conf import settings
from django.conf.urls.static import static


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="post")
# router.register(r'v2/posts', views2.PostViewSet, basename="post2")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # path('v2/posts/',views.get_post_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
