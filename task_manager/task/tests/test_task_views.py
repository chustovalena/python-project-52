import pytest
from django.urls import reverse
from task_manager.task.models import Task
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_index_users(client):
    url = reverse('tasks:index')
    response = client.get(url)

    assert response.status_code == 302
    assert '/login' in response.url


@pytest.mark.django_db
def test_task_index_users_logged(
        client_logged_in, task_factory, user_factory, status_factory):
    status = status_factory(name='first')
    user = user_factory(name='kuku', password='pass')
    task_factory(name='first', author=user, status=status)
    task_factory(name='second')

    url = reverse('tasks:index')
    response = client_logged_in.get(url)

    assert response.status_code == 200
    assert 'task/index.html' in [t.name for t in response.templates]

    tasks = response.context['tasks']
    assert len(tasks) == 2


@pytest.mark.django_db
def test_task_create(client):
    url = reverse('tasks:create')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_task_create_logged(client_logged_in, status_factory, label_factory):
    url = reverse('tasks:create')
    status = status_factory(name='bup')
    label = label_factory(name='dup')
    response = client_logged_in.post(url, data={
        'name': 'New Task',
        'description': 'Desc',
        'status': status.id,
        'executor': '',
        'labels': [label.id],
    }, follow=True)

    assert response.status_code == 200
    assert Task.objects.count() == 1

    task = Task.objects.first()

    assert task.name == 'New Task'
    assert task.author.username == 'logged_user'
    assert task.status == status
    assert label in task.labels.all()
    assert task.executor is None
    assert 'The task was created successfully' in response.content.decode()


@pytest.mark.django_db
def test_task_update_no_login(client, task_factory):
    task = task_factory()
    url = reverse('tasks:update', args=[task.id])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_task_update_view(client_logged_in, task_factory, label_factory):
    task = task_factory(name='Old Task', description='For Update')
    url = reverse('tasks:update', args=[task.id])
    label = label_factory(name='Label')

    data = {
        'name': 'New Task',
        'description': 'For Update',
        'status': task.status.id,
        'labels': [label.id],
        'executor': ''
    }
    response = client_logged_in.post(url, data, follow=True)
    task.refresh_from_db()
    assert response.status_code == 200
    assert task.name == 'New Task'
    assert 'The task was updated successfully' in response.content.decode()


@pytest.mark.django_db
def test_task_delete_requires_login(client, task_factory):
    task = task_factory()
    url = reverse('tasks:delete', args=[task.id])

    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_task_delete_not_author(client_logged_in, task_factory, user_factory):
    user1 = user_factory(usernamme='author', password='pass')
    task = task_factory(author=user1)
    url = reverse('tasks:delete', args=[task.id])

    response = client_logged_in.post(url, follow=True)
    phrase = 'Task can only be deleted by its author'
    assert Task.objects.count() == 1
    assert phrase in response.content.decode()


@pytest.mark.django_db
def test_task_delete_author(client_logged_in, task_factory):
    user = get_user_model().objects.get(username='logged_user')
    task = task_factory(author=user)
    url = reverse('tasks:delete', args=[task.id])

    response = client_logged_in.post(url, follow=True)

    assert Task.objects.count() == 0
    assert 'The task was deleted successfully' in response.content.decode()


@pytest.mark.django_db
def test_task_detail_view_requires_login(client, task_factory):
    task = task_factory()
    url = reverse('tasks:detail', args=[task.id])

    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_task_detail_success(client_logged_in, task_factory):
    task = task_factory(name="Task 1")
    url = reverse('tasks:detail', args=[task.id])

    response = client_logged_in.get(url)

    assert response.status_code == 200
    assert 'task/detail.html' in [t.name for t in response.templates]
    assert response.context["task"].name == "Task 1"
