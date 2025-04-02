from django.shortcuts import render

def index(request):
    """View to return the adoption page"""
    return render(request, 'adoption/adoption.html')