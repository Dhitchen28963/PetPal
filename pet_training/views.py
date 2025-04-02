from django.shortcuts import render

def index(request):
    """View to return the pet training page"""
    return render(request, 'pet_training/pet_training.html')