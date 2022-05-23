from django.urls import reverse
from django.test import Client

from django.contrib.auth.models import User

import faker
import pytest

from .models import Profile

client = Client()
pytestmark = pytest.mark.django_db
faker = faker.Faker()


@pytest.fixture
def profile():
    user = User.objects.create_user(
        username=faker.user_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        password=faker.password(),
    )

    profile = Profile.objects.create(
        user=user,
        favorite_city=faker.city(),
    )

    return profile


def test_index_page(profile):
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200

    assert bytes(profile.user.username, encoding="utf-8") in response.content
    assert b"Home" in response.content
    assert b"Lettings" in response.content


def test_profile_page(profile):
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert response.status_code == 200

    assert bytes(profile.user.first_name, encoding="utf-8") in response.content
    assert bytes(profile.user.last_name, encoding="utf-8") in response.content
