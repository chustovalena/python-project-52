import pytest
from django.urls import reverse
from task_manager.label.models import Label


@pytest.mark.django_db
def test_status_index_requires_login(client):
    url = reverse('labels:index')

    response = client.get(url)

    assert response.status_code == 302
    assert '/login' in response.url


@pytest.mark.django_db
def test_status_index_success(client_logged_in, label_factory):
    label_factory()
    label_factory(name='yeah')
    url = reverse('labels:index')

    response = client_logged_in.get(url)

    assert response.status_code == 200
    assert 'label/index.html' in [t.name for t in response.templates]

    assert len(response.context['labels']) == 2


@pytest.mark.django_db
def test_status_create_requires_login(client):
    url = reverse('labels:create')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_status_create_succes(client_logged_in):
    url = reverse('labels:create')

    response = client_logged_in.post(url, data={
        'name': "My label"
    }, follow=True)

    assert response.status_code == 200
    assert Label.objects.count() == 1

    status = Label.objects.first()

    assert status.name == 'My label'
    assert 'The label was created successfully' in response.content.decode()


@pytest.mark.django_db
def test_status_update_requires_login(client, label_factory):
    label = label_factory(name='hahaha')
    url = reverse('labels:update', args=[label.id])
    response = client.get(url)

    assert response.status_code == 302
    assert '/login' in response.url


@pytest.mark.django_db
def test_status_update_success(client_logged_in, label_factory):
    label = label_factory(name='hey honey')
    url = reverse('labels:update', args=[label.id])

    response = client_logged_in.post(url, data={
        'name': 'hey candy'
    }, follow=True)

    label.refresh_from_db()

    assert response.status_code == 200
    assert Label.objects.count() == 1
    assert label.name == 'hey candy'
    assert 'The label was updated successfully' in response.content.decode()


@pytest.mark.django_db
def test_status_delete_requires_login(client, label_factory):
    status = label_factory(name='help')
    url = reverse('labels:delete', args=[status.id])

    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_status_delete_fk(client_logged_in, task_factory, label_factory):
    label = label_factory(name='Hey')
    task = task_factory()
    task.labels.set([label])
    task.save()
    
    url = reverse('labels:delete', args=[label.id])

    response = client_logged_in.post(url, follow=True)
    label.refresh_from_db()
    phrase = 'It is not possible to delete a label because it is used in tasks.'
    assert phrase in response.content.decode()
    assert Label.objects.count() == 1


@pytest.mark.django_db
def test_status_delete_succes(client_logged_in, label_factory):
    label = label_factory(name='help')
    url = reverse('labels:delete', args=[label.id])

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert Label.objects.count() == 0
    assert 'The label was deleted successfully' in response.content.decode()
