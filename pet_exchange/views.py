from django.shortcuts import render

def index(request):
    """View to return the pet exchange page"""
    return render(request, 'pet_exchange/pet_exchange.html')