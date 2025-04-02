from django.shortcuts import render

def index(request):
    """View to return the pet profiles page"""
    return render(request, 'pet_profiles/pet_profiles.html')