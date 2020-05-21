from django.shortcuts import render

# Create your views here.
def blog(request):
    """A view that displays the blog page"""
    return render(request, "blog.html")