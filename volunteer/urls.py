from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [
    path('', views.index, name='index'),
]