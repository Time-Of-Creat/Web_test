from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tasks.models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


def task_list(request):
    tasks = Task.objects.all().order_by('-creation_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
