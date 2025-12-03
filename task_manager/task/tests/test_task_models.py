import pytest
from django.db.models import ProtectedError

from django.contrib.auth import get_user_model
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.label.models import Label


User = get_user_model()


def test_task_create_and_str(task_factory):
    task = task_factory(name='name', description='desc')

    assert task.id is not None
    assert str(task) == 'name'
    assert task.description == 'desc'
    assert str(task.status) == 'default'
    assert str(task.author) == 'Author user'



def test_labels_many_to_many(task_factory, label_factory):
    l1 = label_factory(name='first l')
    l2 = label_factory(name='second l')

    task = task_factory(name='task')

    task.labels.add(l1, l2)

    assert l1 in task.labels.all()
    assert l2 in task.labels.all()
    assert task in l1.tasks.all()
    assert task in l2.tasks.all()


def test_on_delete_protect(task_factory):
    task = task_factory(name='t1')
    
    with pytest.raises(ProtectedError):
        task.status.delete()
    
    with pytest.raises(ProtectedError):
        task.author.delete()
