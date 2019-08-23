from django.urls import path

# app
from . import views

urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull),
    path('', views.index),
]