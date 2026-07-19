from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from tasks.exceptions import TaskAlreadyCompletedError
from tasks.models import Task


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    try:
        task.complete()
    except TaskAlreadyCompletedError:
        messages.error(request, "Задача {task.title} уже была завершена!")
    
    return redirect('task_list')


def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-creation_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
