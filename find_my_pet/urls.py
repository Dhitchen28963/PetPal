from django.urls import path
from . import views

app_name = 'find_my_pet'

urlpatterns = [
    path('', views.index, name='index'),
]