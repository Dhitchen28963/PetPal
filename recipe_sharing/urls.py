from django.urls import path
from . import views

app_name = 'recipe_sharing'

urlpatterns = [
    path('', views.index, name='index'),
]