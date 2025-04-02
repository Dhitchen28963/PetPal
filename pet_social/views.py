from django.shortcuts import render

def index(request):
    """View to return the pet social page"""
    return render(request, 'pet_social/pet_social.html')