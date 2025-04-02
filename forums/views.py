from django.shortcuts import render

def index(request):
    """View to return the forums page"""
    return render(request, 'forums/forums.html')