from django.urls import path
from . import views

app_name = 'subscription_box'

urlpatterns = [
    path('', views.index, name='index'),
]