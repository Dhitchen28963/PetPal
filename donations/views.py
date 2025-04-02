from django.shortcuts import render

def index(request):
    """View to return the donations page"""
    return render(request, 'donations/donations.html')