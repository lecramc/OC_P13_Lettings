from django.test import Client
from django.urls import reverse


def test_view_code():
    """Check if the view is accessible"""
    client = Client()
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200


def test_view_title():
    """Check if the title is OK"""
    client = Client()
    response = client.get(reverse('profiles:index'))
    assert "Profiles" in str(response.content)
