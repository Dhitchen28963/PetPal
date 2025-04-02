from django.shortcuts import render

def index(request):
    """View to return the user profile page"""
    return render(request, 'profiles/profiles.html')