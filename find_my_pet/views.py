from django.shortcuts import render

def index(request):
    """View to return the find my pet page"""
    return render(request, 'find_my_pet/find_my_pet.html')