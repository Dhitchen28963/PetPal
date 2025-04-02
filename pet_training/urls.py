from django.urls import path
from . import views

app_name = 'pet_training'

urlpatterns = [
    path('', views.index, name='index'),
]