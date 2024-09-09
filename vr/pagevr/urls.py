from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pagevr/", include("pagevr.urls")),
    path("admin/", admin.site.urls),
]