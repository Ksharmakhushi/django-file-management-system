from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.file_upload, name='upload'),
    path('files/', views.file_list,name='file_list'),
    path('download/<int:id>/',views.download_file,name='download'),
]