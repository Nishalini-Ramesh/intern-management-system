# growtern/urls.py

from django.urls import path
from . import views  # Make sure you have at least one view

urlpatterns = [
    path('', views.home, name='home'),  # Replace `home` with your actual view function
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
]
