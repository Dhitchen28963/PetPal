from django.urls import path
from . import views

app_name = 'veterinarian'

urlpatterns = [
    path('', views.index, name='index'),
]