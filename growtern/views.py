import os
from django.shortcuts import render
from django.http import FileResponse, HttpResponse

def home(request):
    return HttpResponse("Welcome to Intern Management System!")

# Dashboard Views
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def intern_dashboard(request):
    return render(request, 'intern_dashboard.html')

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

# Mentor Views
def assign_task(request):
    return render(request, 'create_task.html')

def task_reports(request):
    return render(request, 'task_list.html')

def task_feedback(request):
    return render(request, 'task_feedback.html')

# Intern Views
def submit_task(request):
    return render(request, 'task_submission.html')

def view_tasks(request):
    return render(request, 'upload document.html')  # consider renaming to upload_document.html

def intern_feedback(request):
    return render(request, 'internship report.html')  # consider renaming to internship_report.html

# Download Internship Report
def download_report(request):
    file_path = os.path.join('your_app_name', 'static', 'report.pdf')  # adjust 'your_app_name'
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='intern_report.pdf')
    except FileNotFoundError:
        return HttpResponse("Report file not found.", status=404)
