from django.urls import path
from . import views

app_name = 'compatibility_finder'

urlpatterns = [
    path('', views.index, name='index'),
]