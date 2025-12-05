import pytest
from django.test import RequestFactory
from task_manager.task.filters import TaskFilter
from task_manager.task.models import Task


def test_filter_self_tasks(user_factory, task_factory, status_factory):
    status = status_factory(name='kol')
    user1 = user_factory(username='user1')
    user2 = user_factory(username='user2')

    t1 = task_factory(name='task1', author=user1, status=status)
    task_factory(name='task2', author=user2)

    data = {'self_tasks': True}

    request = RequestFactory().get('/tasks', data)
    request.user = user1

    filtered = TaskFilter(data=data, queryset=Task.objects.all(), request=request)

    assert list(filtered.qs) == [t1]


def test_task_filter_self_false(user_factory, task_factory, status_factory):
    user1 = user_factory()

    status = status_factory(name='kleo')
    task1 = task_factory(name='task1', author=user1, status=status)
    task2 = task_factory(name='task2')

    data = {'self_tasks': False}
    request = RequestFactory().get('/tasks', data)

    filtered = TaskFilter(data=data, queryset=Task.objects.all(), request=request)

    assert set(filtered.qs) == {task1, task2}


def test_task_filter_status(status_factory, task_factory, user_factory):
    status1 = status_factory(name='first')
    task1 = task_factory(status=status1)

    user2 = user_factory(username='user2')
    status2 = status_factory(name='second')
    task_factory(name='task2', status=status2, author=user2)

    data = {'status': status1.id}
    request = RequestFactory().get('/tasks', data)

    filtered = TaskFilter(data=data, queryset=Task.objects.all(), request=request)

    assert list(filtered.qs) == [task1]


def test_task_filter_executor(status_factory, user_factory, task_factory):
    user1 = user_factory(username='user1')
    status1 = status_factory(name='first')

    user2 = user_factory(username='user2')
    status2 = status_factory(name='second')

    task1 = task_factory(name='task1', status=status1, author=user1, executor=user2)
    task2 = task_factory(name='task2', status=status2, author=user2, executor=user1)

    data = {'executor': user1.id}
    request = RequestFactory().get('/tasks', data)

    filtered = TaskFilter(data=data, queryset=Task.objects.all(), request=request)

    assert list(filtered.qs) == [task2]


def test_task_filter_labels(status_factory, label_factory, user_factory, task_factory):
    user1 = user_factory(username='user1')
    status1 = status_factory(name='first')

    label1 = label_factory(name='l1')
    label2 = label_factory(name='l2')

    task1 = task_factory(name='task1', status=status1, author=user1, labels=[label1])
    task2 = task_factory(name='task2', labels=[label2])

    data = {'labels': [label2]}
    request = RequestFactory().get('/tasks', data)

    filtered = TaskFilter(data=data, queryset=Task.objects.all(), request=request)

    assert list(filtered.qs) == [task2]