from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import TaskFilter
from django.shortcuts import redirect
from django.utils.translation import gettext as _

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
        messages.success(self.request, _('The task was created successfully'))
        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/update.html'
    success_url = reverse_lazy('tasks:index')

    def form_valid(self, form):
        messages.success(self.request, _('The task was updated successfully'))
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('tasks:index')
    
    def form_valid(self, form):
        messages.success(self.request, _('The task was deleted successfully'))
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()

        if task.author != request.user:
            messages.error(
                request,
                _('Task can only be deleted by its author')
            )
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/detail.html'
    context_object_name = 'task'
