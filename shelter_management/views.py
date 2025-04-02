from django.shortcuts import render

def index(request):
    """View to return the shelter management page"""
    return render(request, 'shelter_management/shelter_management.html')