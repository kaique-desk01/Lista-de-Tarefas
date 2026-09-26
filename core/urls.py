from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('home/', views.home, name='tasks-home'),
    path('add_task/', views.add_task, name='tasks-add_task'),
    path('concluir/<int:task_id>/', views.task_complete, name='tasks-concluir'),
    path('delete/<int:task_id>/', views.delete_task, name='tasks-delete'),
    path('delete_all/', views.delete_all_tasks, name='tasks-delete_all'),
]