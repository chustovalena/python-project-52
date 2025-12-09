from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.utils.translation import gettext as _


User = get_user_model()

class UserIndexView(ListView):
    model = User
    ordering = ['id']
    template_name = 'user/index.html'
    context_object_name = 'users'
    paginate_by = 15


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "user/create.html"
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        messages.success(self.request, _('The user has been successfully registered'))
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        messages.success(self.request, _('The user was updated successfully'))
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, _("You don't have the rights to change another user."))
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        messages.success(self.request, _('The user was deleted successfully'))
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, _("You don't have the rights to delete another user."))
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)
    

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'user'

