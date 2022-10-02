from django.urls import path, include

urlpatterns = [
    path('v1/', include('mediumpost.urls_1')),
    path('v2/', include('mediumpost.urls_2')),
]