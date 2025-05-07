import uuid

import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def get_user():
    user_model = get_user_model()
    user = user_model.objects.create_user(username="test user")
    user.save()
    return user


@pytest.mark.django_db
def test_custom_user_has_uuid_as_pk(get_user):
    user = get_user
    assert uuid.UUID(str(user.pk))
