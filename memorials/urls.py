from django.urls import path
from . import views

app_name = 'memorials'

urlpatterns = [
    path('', views.index, name='index'),
]