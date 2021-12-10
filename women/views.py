from django.http.response import HttpResponseNotFound, Http404, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
# So here I create something like canvas by creating a function for display it on my web page
# then I add data(model) from models file which content come from db
# then I put templates(structure)


def index(request):
    return HttpResponse("Page of women app")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Articles by Categories</h1><p>{catid}</p>")


# Displaying date
def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Archive of year</h1><p>{year}</p>")


# for 404 cases

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> This page not found 404</h1>")
