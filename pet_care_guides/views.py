from django.shortcuts import render

def index(request):
    """View to return the pet care guides page"""
    return render(request, 'pet_care_guides/pet_care_guides.html')