import pytest
from task_manager.user.forms import CustomUserCreationForm, CustomUserUpdateForm


def test_user_create_form_fields():
    form = CustomUserCreationForm()

    test_fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    for f in test_fields:
        assert f in form.fields


@pytest.mark.django_db
def test_user_create_valid_form():
    form = CustomUserCreationForm(data={
        'first_name': 'Ukulele',
        'last_name': 'Skripka',
        'username': 'Fortepiano',
        'password1': 'HelloMusik',
        'password2': 'HelloMusik'
    })

    assert form.is_valid()


@pytest.mark.django_db
def test_user_create_invalid_form():
    form = CustomUserCreationForm(data={
        'first_name': 'Ukulele',
        'last_name': 'Skripka',
        'username': 'Fortepiano',
        'password1': 'Hello',
        'password2': 'Hello'
    })

    assert not form.is_valid()
    assert 'password2' in form.errors


@pytest.mark.django_db
def test_user_create_password_didnt_match():
    form = CustomUserCreationForm(data={
        'first_name': 'Ukulele',
        'last_name': 'Skripka',
        'username': 'Fortepiano',
        'password1': 'HelloDarling',
        'password2': 'HelloEvil'
    })

    assert not form.is_valid()
    assert 'password2' in form.errors


@pytest.mark.django_db
def test_user_update_form_valid(user_factory):
    user = user_factory(username='old_one')

    form = CustomUserUpdateForm(instance=user, data={
        'first_name': 'Leon',
        'last_name': 'Gates',
        'username': 'old_one',
        'password1': 'passpass1',
        'password2': 'passpass1'
    })

    assert form.is_valid()


def test_user_update_form_valid(user_factory):
    user1 = user_factory(username='first')
    user_factory(username='second')

    form = CustomUserUpdateForm(
        instance=user1,
        data={
            'first_name': 'Leon',
            'last_name': 'Gates',
            'username': 'second',
            'password1': 'passpass1',
            'password2': 'passpass1'
        }
    )

    assert not form.is_valid()
    assert 'username' in form.errors
