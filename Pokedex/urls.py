from django.urls import path, include
from django import views
from Pokedex import views

urlpatterns = [
    path('/', views.inicio, name='inicio')
]
