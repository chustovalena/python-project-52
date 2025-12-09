import django_filters
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):

    self_tasks = django_filters.BooleanFilter(
        label=_('Only my tasks'),
        method='filter_self_tasks',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.get('request')
        super().__init__(*args, **kwargs)

        self.form.fields['status'].widget.attrs.update({
            'class': 'form-select form-control'
        })
        self.form.fields['executor'].widget.attrs.update({
            'class': 'form-select form-control'
        })
        self.form.fields['labels'].widget = forms.Select(attrs={
            'class': 'form-select form-control'
        })

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
