from django.shortcuts import render

def index(request):
    """View to return the grooming page"""
    return render(request, 'grooming/grooming.html')