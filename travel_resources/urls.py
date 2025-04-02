from django.urls import path
from . import views

app_name = 'travel_resources'

urlpatterns = [
    path('', views.index, name='index'),
]