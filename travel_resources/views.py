from django.shortcuts import render

def index(request):
    """View to return the travel resources page"""
    return render(request, 'travel_resources/travel_resources.html')