from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import TaskForm
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import TaskFilter

class TaskIndexView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'task/index.html'
    ordering = ['id']
    context_object_name = 'tasks'
    paginate_by = 15
    filterset_class = TaskFilter


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')
    template_name = 'task/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Задача создана')
        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/update.html'
    success_url = reverse_lazy('tasks:index')


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('tasks:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/detail.html'
    context_object_name = 'task'