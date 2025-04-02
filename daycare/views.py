from django.shortcuts import render

def index(request):
    """View to return the daycare page"""
    return render(request, 'daycare/daycare.html')