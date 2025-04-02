from django.shortcuts import render

def index(request):
    """View to return the subscription box page"""
    return render(request, 'subscription_box/subscription_box.html')