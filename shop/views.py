from django.shortcuts import render

def index(request):
    """View to return the shop page"""
    return render(request, 'shop/shop.html')