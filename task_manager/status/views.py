from .models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomStatusCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


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
        messages.success(self.request, _('The status was created successfully'))
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = CustomStatusCreationForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses:index')

    def form_valid(self, form):
        messages.success(self.request, _('The status was updated successfully'))
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('statuses:index')

    def form_valid(self, form):
        status = self.get_object()

        if status.task_set.exists():
            messages.error(self.request, _("Status is used by tasks."))
            return redirect(self.success_url)
        messages.success(self.request, _('The status was deleted successfully'))
        return super().form_valid(form)
