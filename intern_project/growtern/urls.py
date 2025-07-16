# growtern/urls.py

from django.urls import path
from . import views  # Make sure you have at least one view

urlpatterns = [
    path('', views.home, name='home'),  # Replace `home` with your actual view function
]
