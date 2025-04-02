from django.shortcuts import render

def index(request):
    """View to return the compatibility finder page"""
    return render(request, 'compatibility_finder/compatibility_finder.html')