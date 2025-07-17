from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Dashboard routes
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor_dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern_dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),

    # Mentor-specific routes
    path('assign_task/', views.assign_task, name='assign_task'),
    path('task_reports/', views.task_reports, name='task_reports'),
    path('task_feedback/', views.task_feedback, name='task_feedback'),

    # Intern-specific routes
    path('submit_task/', views.submit_task, name='submit_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('intern_feedback/', views.intern_feedback, name='intern_feedback'),
]
