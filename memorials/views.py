from django.shortcuts import render

def index(request):
    """View to return the memorials page"""
    return render(request, 'memorials/memorials.html')