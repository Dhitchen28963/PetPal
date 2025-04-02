from django.shortcuts import render

def index(request):
    """View to return the pet health page"""
    return render(request, 'pet_health/pet_health.html')