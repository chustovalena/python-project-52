from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import MyAuthenticationForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"
    form_class = MyAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, _("You have successfully logged into your account!"))
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You have successfully logged out of your account"))
        return super().dispatch(request, *args, **kwargs)
