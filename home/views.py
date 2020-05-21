from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def favourites(request):
    return render(request, "favourites.html")
