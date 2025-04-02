from django.urls import path
from . import views

app_name = 'training_tips'

urlpatterns = [
    path('', views.index, name='index'),
]