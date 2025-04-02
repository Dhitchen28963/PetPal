from django.shortcuts import render

def index(request):
    """View to return the FAQ page"""
    return render(request, 'faq/faq.html')