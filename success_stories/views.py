from django.shortcuts import render

def index(request):
    """View to return the success stories page"""
    return render(request, 'success_stories/success_stories.html')