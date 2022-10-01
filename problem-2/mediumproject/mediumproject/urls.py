from django.contrib import admin
from django.urls import path, include

import blog

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("blog.urls"))
]
