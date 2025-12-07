import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.messages import get_messages


User = get_user_model()

@pytest.mark.django_db
def test_user_create_view(client):
    url = reverse('users:create')

    data = {
        'first_name': 'Draco',
        'last_name': 'Malfoy',
        'username': 'BigOne',
        'password1': 'passdraco1',
        'password2': 'passdraco1',
    }

    response = client.post(url, data, follow=True)

    assert response.status_code == 200
    assert User.objects.count() == 1
    assert User.objects.filter(username='BigOne').exists()
    assert 'The user has been successfully registered' in response.content.decode()


@pytest.mark.django_db
def test_user_update_other(user_factory, client_logged_in):
    user = user_factory()
    url = reverse('users:update', args=[user.id])

    response = client_logged_in.get(url, follow=True)
    print(response.content.decode())

    msgs = [m.message for m in get_messages(response.wsgi_request)]
    assert "You don't have the rights to change another user." in msgs
    assert response.redirect_chain
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_update_self(client_logged_in):
    user = User.objects.get(username='logged_user')
    url = reverse('users:update', args=[user.id])

    response = client_logged_in.post(url, data={
        'first_name': 'Tom',
        'last_name': 'Riddle',
        'username': 'logged_user',
        'password1': 'passworddarklord',
        'password2': 'passworddarklord',
    }, follow=True)

    assert response.status_code == 200
    assert User.objects.count() == 1
    assert User.objects.filter(username="logged_user").exists()
    assert 'The user was updated successfully' in response.content.decode()


@pytest.mark.django_db
def test_user_delete_forbidden(client_logged_in, user_factory):
    other = user_factory(username='Dracula')
    url = reverse('users:delete', args=[other.id])

    response = client_logged_in.post(url, follow=True)
    print(response.content.decode())

    assert response.status_code == 200
    assert User.objects.filter(username='Dracula').exists()
    assert User.objects.filter(username='logged_user').exists()
    msgs = [m.message for m in get_messages(response.wsgi_request)]
    assert "You don't have the rights to delete another user." in msgs


@pytest.mark.django_db
def test_user_delete_self(client_logged_in, user_factory):
    user = User.objects.get(username='logged_user')
    url = reverse('users:delete', args=[user.id])

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert not User.objects.filter(username='logged_user').exists()
    assert User.objects.count() == 0
    assert 'The user was deleted successfully' in response.content.decode()
