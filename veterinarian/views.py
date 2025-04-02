from django.shortcuts import render

def index(request):
    """View to return the veterinarian page"""
    return render(request, 'veterinarian/veterinarian.html')