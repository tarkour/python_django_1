from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(respond):
    return HttpResponse('<h1>Aloha, Denis!</h1>')