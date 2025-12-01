from django.urls import path
from .views import TaskIndexView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView


urlpatterns = [
    path('', TaskIndexView.as_view(), name='index'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/update', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name='delete'),
]