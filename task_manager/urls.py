from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('users/', include(('task_manager.user.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),
]

