from django.urls import path
from . import views

app_name = 'shelter_management'

urlpatterns = [
    path('', views.index, name='index'),
]