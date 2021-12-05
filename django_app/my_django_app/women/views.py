from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# So here I create something like canvas by creating a function for display it on my web page
# then I add data(model) from models file which content come from db
# then I put templates(structure)


def index(request):
    return HttpResponse("Page of women app")


def categories(request, catid):
    return HttpResponse(f"<h1>Articles by Categories</h1><p>{catid}</p>")
