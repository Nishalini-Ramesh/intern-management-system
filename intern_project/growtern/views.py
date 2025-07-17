from django.shortcuts import render, redirect

# Temporary memory-based task list
task_store = []

def home(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def task_list(request):
    return render(request, 'task_list.html', {'tasks': task_store})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task_store.append({'title': title, 'completed': False})
        return redirect('task_list')
    return render(request, 'create_task.html')

def intern_list(request):
    return render(request, 'intern_list.html')

def add_intern(request):
    return render(request, 'add_intern.html')

def edit_intern(request):
    return render(request, 'edit_intern.html')

def assign_mentor(request):
    return render(request, 'assign_mentor.html')