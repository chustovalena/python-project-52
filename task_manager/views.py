from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно вошли в аккаунт!")
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = "login"

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из аккаунта")
        return super().dispatch(request, *args, **kwargs)
