from django.shortcuts import render

def index(request):
    """View to return the pet personality page"""
    return render(request, 'pet_personality/pet_personality.html')