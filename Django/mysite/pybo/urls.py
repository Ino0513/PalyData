from django.urls import path

from . import views

# pybo/urls

urlpatterns = [
    path('', views.index),
]