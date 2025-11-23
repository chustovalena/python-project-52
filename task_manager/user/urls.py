from django.urls import path
from .views import UserIndexView, UserCreateView, UserUpdateView, UserDeleteView


urlpatterns = [
    path("", UserIndexView.as_view(), name='index'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]
