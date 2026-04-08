

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# READ + CREATE
def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')  # 📅 get date

        if title:
            Task.objects.create(
                title=title,
                due_date=due_date if due_date else None  # save date
            )

        return redirect('task_list')

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# UPDATE
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'task': task})


# DELETE
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/delete_task.html', {'task': task})

from django.http import JsonResponse

def toggle_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'success', 'completed': task.completed})

def task_history(request):
    tasks = Task.objects.filter(completed=True).order_by('-created_at')
    return render(request, 'tasks/history.html', {'tasks': tasks})


def tasks_by_date(request):
    date = request.GET.get('date')
    
    if date:
        tasks = Task.objects.filter(due_date=date)
    else:
        tasks = []

    return render(request, 'tasks/by_date.html', {'tasks': tasks})