from django.shortcuts import render

def index(request):
    """View to return the training tips page"""
    return render(request, 'training_tips/training_tips.html')