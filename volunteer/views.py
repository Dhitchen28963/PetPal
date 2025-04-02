from django.shortcuts import render

def index(request):
    """View to return the volunteer page"""
    return render(request, 'volunteer/volunteer.html')