from django.shortcuts import render
from tasks.models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-creation_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
