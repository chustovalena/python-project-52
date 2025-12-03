from task_manager.status.models import Status



def test_status_create_and_str(status_factory):
    status = status_factory(name='first status')

    assert status.id is not None
    assert str(status) == 'first status'
