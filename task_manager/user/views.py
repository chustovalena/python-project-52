from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserUpdateForm


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
    success_url = reverse_lazy("users:index")
    
    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно изменен')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users:index')

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно удален')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)
    

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'user'

