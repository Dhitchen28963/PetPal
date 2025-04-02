from django.urls import path
from . import views

app_name = 'daycare'

urlpatterns = [
    path('', views.index, name='index'),
]