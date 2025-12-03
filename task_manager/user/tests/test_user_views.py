import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


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
    assert 'Пользователь успешно зарегистрирован' in response.content.decode()


@pytest.mark.django_db
def test_user_update_other(user_factory, client_logged_in):
    user = user_factory()
    url = reverse('users:update', args=[user.id])

    response = client_logged_in.get(url, follow=True)

    assert "У вас нет прав для изменения другого пользователя." in response.content.decode()
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
    assert 'Пользователь успешно изменен' in response.content.decode()


@pytest.mark.django_db
def test_user_delete_forbidden(client_logged_in, user_factory):
    other = user_factory(username='Dracula')
    url = reverse('users:delete', args=[other.id])

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert "У вас нет прав для изменения другого пользователя." in response.content.decode()
    assert User.objects.filter(username='Dracula').exists()
    assert User.objects.filter(username='logged_user').exists()


@pytest.mark.django_db
def test_user_delete_self(client_logged_in, user_factory):
    user = User.objects.get(username='logged_user')
    url = reverse('users:delete', args=[user.id])

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert not User.objects.filter(username='logged_user').exists()
    assert User.objects.count() == 0
    assert 'Пользователь успешно удален' in response.content.decode()



