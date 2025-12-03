from task_manager.status.models import Status
from task_manager.label.models import Label
from task_manager.task.models import Task
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def client_logged_in(client, user_factory):
    user = user_factory(username='logged_user', password='testpass')
    client.login(username=user.username, password='testpass')
    return client


@pytest.fixture
def user_factory(db):
    def create_user(**kwargs):
        username = kwargs.get('username', 'test_user')
        password = kwargs.get('password', 'pass')
        return User.objects.create_user(
            username=username,
            password=password
        )
    return create_user


@pytest.fixture
def status_factory(db):
    def create_status(**kwargs):
        name = kwargs.get('name', 'Test Status')
        return Status.objects.create(name=name)
    return create_status


@pytest.fixture
def label_factory(db):
    def create_label(**kwargs):
        name = kwargs.get('name', 'Test Label')
        return Label.objects.create(name=name)
    return create_label


@pytest.fixture
def task_factory(db, status_factory, user_factory):
    def create_task(**kwargs):
        status = kwargs.get('status') or status_factory(name='default')
        author = kwargs.get('author') or user_factory(username='Author user')
        executor = kwargs.get('executor')
        name = kwargs.get('name', 'Test Task')
        description = kwargs.get('description', 'Test Task Description')

        task = Task.objects.create(
            name=name,
            description=description,
            status=status,
            author=author,
            executor=executor
        )

        labels = kwargs.get('labels')
        if labels:
            task.labels.set(labels)
        
        return task
    return create_task
