from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LabelForm
from django.contrib import messages
from django.utils.translation import gettext as _



class LabelIndexView(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'label/index.html'
    ordering = ['id']
    paginate_by = 15


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    template_name = 'label/create.html'

    def form_valid(self, form):
        messages.success(self.request, _('The label was created successfully'))
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    template_name = 'label/update.html'

    def form_valid(self, form):
        messages.success(self.request, _('The label was updated successfully'))
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label/delete.html'
    success_url = reverse_lazy('labels:index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.tasks.exists():
            messages.error(request, _('It is not possible to delete a label because it is used in tasks.'))
            return redirect(self.success_url)
        messages.success(request,  _('The label was deleted successfully'))
        return super().post(request, *args, **kwargs)



