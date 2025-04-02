from django.urls import path
from . import views

app_name = 'pet_insurance'

urlpatterns = [
    path('', views.index, name='index'),
]