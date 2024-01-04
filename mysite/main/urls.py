# define path to different web-pages

from django.urls import path
from . import views #import views from current directory

urlpatterns = [
    path('<str:name>', views.index, name='index'), #if go to adress without any '/' after '.com'
                                         # redirect you to '.com' + 'index' and return a func 'index' from views.py
    path('', views.home, name='home')
]