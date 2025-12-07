from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import MyAuthenticationForm
from django.http import HttpResponse


def rollbar_test(request):
    a = None
    a.hello()  # намеренная ошибка
    return HttpResponse("Rollbar test")


class HomePageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"
    form_class = MyAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно вошли в аккаунт!")
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = "login"

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из аккаунта")
        return super().dispatch(request, *args, **kwargs)
