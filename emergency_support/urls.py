from django.urls import path
from . import views

app_name = 'emergency_support'

urlpatterns = [
    path('', views.index, name='index'),
]