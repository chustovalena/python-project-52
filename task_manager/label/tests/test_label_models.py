from task_manager.label.models import Label


def test_label_create_and_str(label_factory):
    label = label_factory(name='first')

    assert label.id is not None
    assert str(label) == 'first'