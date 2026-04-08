from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('history/', views.task_history, name='task_history'),
    path('by-date/', views.tasks_by_date, name='tasks_by_date'),
]