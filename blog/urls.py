from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('file/upload', views.file_upload, name='file_upload'),
]