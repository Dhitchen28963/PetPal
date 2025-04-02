from django.shortcuts import render

def index(request):
    """View to return the events page"""
    return render(request, 'events/events.html')