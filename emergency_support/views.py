from django.shortcuts import render

def index(request):
    """View to return the emergency support page"""
    return render(request, 'emergency_support/emergency_support.html')