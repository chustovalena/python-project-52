from task_manager.task.forms import TaskForm
import pytest


def test_form_fields():
    form = TaskForm()

    test_fields = ['name', 'description', 'status', 'executor', 'labels']

    for f in test_fields:
        assert f in form.fields
    
    assert form.fields['labels'].widget.__class__.__name__ == 'SelectMultiple'


def test_task_form_valid(status_factory, user_factory, label_factory):
    status = status_factory()
    executor = user_factory()
    label1 = label_factory()
    label2 = label_factory(name='second')

    form = TaskForm(data={
        'name': 'Task F',
        'description': 'desc',
        'status': status.id,
        'executor': executor.id,
        'labels': [label1.id, label2.id]
    })

    assert form.is_valid()


def test_task_form_invalid(status_factory):
    status = status_factory()

    form = TaskForm(data={
        'name': '',
        'description': 'Desc',
        'status': status.id,
        'executor': '',
        'labels': []
    })

    assert not form.is_valid()
    assert 'name' in form.errors


@pytest.mark.django_db
def test_task_form_invalid_status():
    form = TaskForm(data={
        'name': 'Test',
        'description': 'Desc',
        'status': 99999,
        'executor': '',
        'labels': []
    })

    assert not form.is_valid()
    assert 'status' in form.errors


def test_task_form_save(status_factory, label_factory, user_factory):
    status = status_factory()
    author = user_factory(username='author')
    executor = user_factory()
    label1 = label_factory(name='second')
    label2 = label_factory()

    form = TaskForm(data={
        'name': 'Test',
        'description': 'desc',
        'executor': executor.id,
        'status': status.id,
        'labels': [label1.id, label2.id]
    })

    assert form.is_valid()

    task = form.save(commit=False)
    task.author = author
    task.save()
    form.save_m2m()

    assert task.name == 'Test'
    assert task.status == status
    assert task.executor == executor
    assert list(task.labels.all()) == [label1, label2]
