from django.urls import path
from .views import (
    LabelIndexView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView
)


urlpatterns = [
    path('', LabelIndexView.as_view(), name='index'),
    path('create/', LabelCreateView.as_view(), name='create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete'),
]