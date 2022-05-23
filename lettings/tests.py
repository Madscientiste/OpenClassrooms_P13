from django.urls import reverse
from django.test import Client

import faker
import pytest

from .models import Letting, Address

client = Client()
pytestmark = pytest.mark.django_db
faker = faker.Faker()


@pytest.fixture
def letting():
    address = Address.objects.create(
        number=faker.random_int(min=1, max=9999),
        street=faker.street_name(),
        city=faker.city(),
        state=faker.state(),
        zip_code=faker.random_int(min=1, max=99999),
        country_iso_code=faker.country_code(),
    )

    letting = Letting.objects.create(
        title="SomTitle",
        address=address,
    )

    return letting


def test_index_page(letting):
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200

    assert bytes(letting.title, encoding="utf-8") in response.content
    assert b"Home" in response.content
    assert b"Profiles" in response.content


def test_letting_page(letting):
    response = client.get(reverse("lettings:letting", args=[letting.pk]))
    assert response.status_code == 200

    assert bytes(letting.title, encoding="utf-8") in response.content
    assert bytes(letting.address.street, encoding="utf-8") in response.content
