from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Page of women app")

def categories(request):
    return HttpResponse("<h1>Articles by Categories</h1>")