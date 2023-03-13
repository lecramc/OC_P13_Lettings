import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_view_code():
    client = Client()
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_title():
    client = Client()
    response = client.get(reverse('lettings:index'))
    assert "Lettings" in str(response.content)
