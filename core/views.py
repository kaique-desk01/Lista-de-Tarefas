from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'tarefas/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task criada com sucesso!!")
            return redirect('tasks:tasks-home')
    else:
        form = TaskForm()
    return render(request, 'tarefas/add_task.html', {'form': form})

@require_POST
def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    if task.completed:
        messages.success(request, "Task concluida com sucesso!!")
    task.save()

    return redirect('tasks:tasks-home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deletada com sucesso!!")
    return redirect('tasks:tasks-home')

def delete_all_tasks(request):
    Task.objects.all().delete()
    messages.success(request, "Tasks deletadas com sucesso!!")
    return redirect('tasks:tasks-home')