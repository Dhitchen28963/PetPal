from django.urls import path
from . import views

app_name = 'adoption'

urlpatterns = [
    path('', views.index, name='index'),
]