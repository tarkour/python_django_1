# define path to different web-pages

from django.urls import path
from . import views #import views from current directory

urlpatterns = [
    path('', views.index(), name='index'),
]