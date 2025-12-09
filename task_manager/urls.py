from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('users/', include(
        ('task_manager.user.urls', 'users'), namespace='users')
    ),
    path('statuses/', include(
        ('task_manager.status.urls', 'statuses'), namespace='statuses')
    ),
    path('tasks/', include(
        ('task_manager.task.urls', 'tasks'), namespace='tasks')
    ),
    path('labels/', include(
        ('task_manager.label.urls', 'labels'), namespace='labels')
    ),
    path('admin/', admin.site.urls),
]

