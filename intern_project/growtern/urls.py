from django.urls import path
from . import views

urlpatterns = [
    path('', views.intern_list, name='home'),
    path('interns/', views.intern_list, name='intern_list'),
    path('add/', views.add_intern, name='add_intern'),
    path('edit/', views.edit_intern, name='edit_intern'),
    path('assign_mentor/', views.assign_mentor, name='assign_mentor'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
]
