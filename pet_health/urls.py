from django.urls import path
from . import views

app_name = 'pet_health'

urlpatterns = [
    path('', views.index, name='index'),
]