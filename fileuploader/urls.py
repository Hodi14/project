from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload, name='upload'),
    path('upload/crop', views.crop, name='crop'),
    path('upload/rotate', views.rotate, name='rotate'),
    path('upload/resize', views.resize, name='resize'),
    path('upload/black_white', views.black_white, name='black_white'),
    path('upload/share', views.share, name='share'),
    path('upload/new_photo/', views.share, name='new_photo'),
]

