from django.shortcuts import render

def index(request):
    """View to return the sitters page"""
    return render(request, 'sitters/sitters.html')