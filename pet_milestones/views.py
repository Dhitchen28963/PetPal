from django.shortcuts import render

def index(request):
    """View to return the pet milestones page"""
    return render(request, 'pet_milestones/pet_milestones.html')