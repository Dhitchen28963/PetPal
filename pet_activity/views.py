from django.shortcuts import render

def index(request):
    """View to return the pet activity page"""
    return render(request, 'pet_activity/pet_activity.html')