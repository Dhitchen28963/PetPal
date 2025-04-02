from django.shortcuts import render

def index(request):
    """View to return the accessories design page"""
    return render(request, 'accessories_design/accessories.html')