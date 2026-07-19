from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib import messages

from tasks.exceptions import TaskAlreadyCompletedError
from tasks.models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    try:
        task.complete()
    except TaskAlreadyCompletedError:
        messages.error(request, "Задача {task.title} уже была завершена!")
    
    return redirect('task_list')


def task_list(request):
    tasks = Task.objects.all().order_by('-creation_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
