from django.urls import reverse
from django.test import Client

client = Client()


def test_index_page():
    response = client.get(reverse("index"))

    assert response.status_code == 200

    assert b"Welcome to " in response.content
    assert b"Lettings" in response.content
    assert b"Profiles" in response.content
