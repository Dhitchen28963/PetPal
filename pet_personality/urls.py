from django.urls import path
from . import views

app_name = 'pet_personality'

urlpatterns = [
    path('', views.index, name='index'),
]