from django.shortcuts import render
from tasks.models import Task

def task_index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "tasks/task_index.html", context)

def task_detail(request,pk):
    task = Task.objects.get(pk=pk)
    context = {
        "task": task
    }
    return render(request, "tasks/task_detail.html",context)