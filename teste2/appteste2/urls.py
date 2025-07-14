from django.urls import path 
from . import views

urlpatterns = [
    path('', views.viewteste, name='viewteste'),
    path('view/', views.viewteste2, name='viewteste2'),
]