import uuid

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from glucose_levels.models import GlucoseLevel


@pytest.fixture
def user_a():
    user_model = get_user_model()
    user_uuid = uuid.uuid4()
    return user_model.objects.create_user(id=user_uuid, username=user_uuid)


@pytest.fixture
def user_b():
    user_model = get_user_model()
    user_uuid = uuid.uuid4()
    return user_model.objects.create_user(id=user_uuid, username=user_uuid)


@pytest.fixture
def user_c():
    user_model = get_user_model()
    user_uuid = uuid.uuid4()
    return user_model.objects.create_user(id=user_uuid, username=user_uuid)


@pytest.fixture
def test_db_six_items(user_a, user_b, user_c):
    # TODO: use factory boy to create these objects instead

    device = "FreeStyle LibreLink"
    serial_number_a = uuid.uuid4()
    serial_number_b = uuid.uuid4()
    serial_number_c = uuid.uuid4()
    record_type = 0

    GlucoseLevel.objects.create(
        user=user_a,
        device=device,
        serial_number=serial_number_a,
        device_timestamp="2021-02-18 10:57",
        record_type=record_type,
        glucose_value_trend=77,
    )
    GlucoseLevel.objects.create(
        user=user_a,
        device=device,
        serial_number=serial_number_a,
        device_timestamp="2021-02-18 11:12",
        record_type=record_type,
        glucose_value_trend=78,
    )
    GlucoseLevel.objects.create(
        user=user_b,
        device=device,
        serial_number=serial_number_b,
        device_timestamp="2021-02-18 11:19",
        record_type=record_type,
        glucose_value_trend=97,
    )
    GlucoseLevel.objects.create(
        user=user_b,
        device=device,
        serial_number=serial_number_b,
        device_timestamp="2021-02-18 11:34",
        record_type=record_type,
        glucose_value_trend=96,
    )
    GlucoseLevel.objects.create(
        user=user_c,
        device=device,
        serial_number=serial_number_c,
        device_timestamp="2021-02-10 09:08",
        record_type=record_type,
        glucose_value_trend=138,
    )
    GlucoseLevel.objects.create(
        user=user_c,
        device=device,
        serial_number=serial_number_c,
        device_timestamp="2021-02-10 09:25",
        record_type=record_type,
        glucose_value_trend=139,
    )


@pytest.fixture
def list_url():
    return reverse("levels_list_view")


def get_item_url(id):
    """not a fixture because id has to be passed to it"""
    return reverse("levels_item_view", args=(id,))


@pytest.mark.django_db
def test_list_url(list_url, test_db_six_items):
    client = APIClient()

    response = client.get(list_url)

    assert response.json()["count"] == 6


@pytest.mark.django_db
def test_list_url_filter_user(list_url, test_db_six_items, user_a):
    client = APIClient()
    filter_url = f"{list_url}?user={user_a.id}"

    response = client.get(filter_url)

    json_object = response.json()
    assert json_object["count"] == 2
    assert json_object["results"][0]["user"] == str(user_a.id)
    assert json_object["results"][1]["user"] == str(user_a.id)

@pytest.mark.django_db
def test_item_url(test_db_six_items, user_a, user_b, user_c):
    client = APIClient()
    first_item_url = get_item_url(1)
    third_item_url = get_item_url(3)
    last_item_url = get_item_url(6)

    response = client.get(first_item_url)

    json_object = response.json()
    assert json_object['user'] == str(user_a.id)
    assert json_object['glucose_value_trend'] == 77

    response = client.get(third_item_url)

    json_object = response.json()
    assert json_object['user'] == str(user_b.id)
    assert json_object['glucose_value_trend'] == 97

    response = client.get(last_item_url)

    json_object = response.json()
    assert json_object['user'] == str(user_c.id)
    assert json_object['glucose_value_trend'] == 139
