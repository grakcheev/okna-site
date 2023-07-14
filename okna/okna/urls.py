# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('catalog.urls', namespace='catalog')),
    path("admin/", admin.site.urls),

]
