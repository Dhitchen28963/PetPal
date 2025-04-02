from django.shortcuts import render

def index(request):
    """View to return the pet insurance page"""
    return render(request, 'pet_insurance/pet_insurance.html')