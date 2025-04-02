from django.shortcuts import render

def index(request):
    """View to return the messaging page"""
    return render(request, 'messaging/messaging.html')