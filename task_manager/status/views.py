from .models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomStatusCreationForm
from django.contrib import messages


# Create your views here.
class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    ordering = ['id']
    template_name = 'status/index.html'
    context_object_name = 'statuses'
    paginate_by = 15


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = CustomStatusCreationForm
    template_name = "status/create.html"
    success_url = reverse_lazy("statuses:index")

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно добавлен')
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = CustomStatusCreationForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses:index')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно изменен')
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('statuses:index')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно удален')
        return super().form_valid(form)
