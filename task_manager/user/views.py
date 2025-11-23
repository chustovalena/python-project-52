from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm


# Create your views here.
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
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('users:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, "Вы можете редактировать только свой профиль")
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, "Вы можете удалить только свой профиль")
            return redirect('users:list')
        return super().dispatch(request, *args, **kwargs)
