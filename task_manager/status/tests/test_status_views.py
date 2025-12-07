from django.urls import reverse
import pytest
from task_manager.status.models import Status


@pytest.mark.django_db
def test_status_index_requires_login(client):
    url = reverse('statuses:index')

    response = client.get(url)

    assert response.status_code == 302
    assert '/login' in response.url


@pytest.mark.django_db
def test_status_index_success(client_logged_in, status_factory):
    status_factory()
    status_factory(name='yeah')
    url = reverse('statuses:index')

    response = client_logged_in.get(url)

    assert response.status_code == 200
    assert 'status/index.html' in [t.name for t in response.templates]

    assert len(response.context['statuses']) == 2


@pytest.mark.django_db
def test_status_create_requires_login(client):
    url = reverse('statuses:create')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_status_create_succes(client_logged_in):
    url = reverse('statuses:create')

    response = client_logged_in.post(url, data={
        'name': "My status"
    }, follow=True)

    assert response.status_code == 200
    assert Status.objects.count() == 1

    status = Status.objects.first()

    assert status.name == 'My status'
    assert 'The status was created successfully' in response.content.decode()


@pytest.mark.django_db
def test_status_update_requires_login(client, status_factory):
    status = status_factory(name='hahaha')
    url = reverse('statuses:update', args=[status.id])
    response = client.get(url)

    assert response.status_code == 302
    assert '/login' in response.url


@pytest.mark.django_db
def test_status_update_success(client_logged_in, status_factory):
    status = status_factory(name='hey honey')
    url = reverse('statuses:update', args=[status.id])

    response = client_logged_in.post(url, data={
        'name': 'hey candy'
    }, follow=True)

    status.refresh_from_db()

    assert response.status_code == 200
    assert Status.objects.count() == 1
    assert status.name == 'hey candy'
    assert 'The status was updated successfully' in response.content.decode()


@pytest.mark.django_db
def test_status_delete_requires_login(client, status_factory):
    status = status_factory(name='help')
    url = reverse('statuses:delete', args=[status.id])

    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_status_delete_fk(client_logged_in, task_factory, status_factory):
    status = status_factory(name='Hey')
    task = task_factory(status=status)
    task.save()
    url = reverse('statuses:delete', args=[status.id])

    response = client_logged_in.post(url, follow=True)
    status.refresh_from_db()

    assert "The status that is used by tasks cannot be deleted." in response.content.decode()
    assert Status.objects.count() == 1


@pytest.mark.django_db
def test_status_delete_succes(client_logged_in, status_factory):
    status = status_factory(name='help')
    url = reverse('statuses:delete', args=[status.id])

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert Status.objects.count() == 0
    assert 'The status was deleted successfully' in response.content.decode()
