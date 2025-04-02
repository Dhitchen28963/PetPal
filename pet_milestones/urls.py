from django.urls import path
from . import views

app_name = 'pet_milestones'

urlpatterns = [
    path('', views.index, name='index'),
]