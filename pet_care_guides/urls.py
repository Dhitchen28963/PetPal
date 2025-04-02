from django.urls import path
from . import views

app_name = 'pet_care_guides'

urlpatterns = [
    path('', views.index, name='index'),
]