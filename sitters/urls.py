from django.urls import path
from . import views

app_name = 'sitters'

urlpatterns = [
    path('', views.index, name='index'),
]