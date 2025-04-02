from django.shortcuts import render

def index(request):
    """View to return the recipe sharing page"""
    return render(request, 'recipe_sharing/recipe_sharing.html')