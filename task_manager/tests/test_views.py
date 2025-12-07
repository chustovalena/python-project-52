import pytest
from django.urls import reverse
from django.contrib.messages import get_messages

@pytest.mark.django_db
def test_home_page_view(client):
    url = reverse('home')

    response = client.get(url)
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_login_post_view(client, user_factory):
    user = user_factory(username='cobi', password='nana')
    url = reverse('login')

    response = client.post(url, {
        'username': user.username,
        'password': 'nana'
    }, follow=True)

    assert response.status_code == 200
    
    msgs = list(get_messages(response.wsgi_request))
    assert len(msgs) == 1
    assert str(msgs[0]) == "You have successfully logged into your account!"


@pytest.mark.django_db
def test_login_wrong_password(client, user_factory):
    user = user_factory(username='cobi', password='pass')
    url = reverse('login')

    response = client.post(url, {
        'username': user.username,
        'password': 'wrong'
    })

    assert response.status_code == 200
    assert "registration/login.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_logout(client_logged_in):
    url = reverse('logout')

    response = client_logged_in.post(url, follow=True)

    assert response.status_code == 200
    assert response.redirect_chain

    msgs = list(get_messages(response.wsgi_request))
    assert len(msgs) == 1
    assert str(msgs[0]) == "You have successfully logged out of your account"