from django.db import models
from django.contrib.auth import get_user_model
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    description = models.TextField(blank=True)

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status')
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks'
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks',
        null=True,
        blank=True,
        verbose_name=_('Executor')
    )

    created_at = models.DateTimeField(auto_now_add=True)

    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        null=True,
        blank=True,
        verbose_name=_('Labels')
    )

    def __str__(self):
        return self.name
