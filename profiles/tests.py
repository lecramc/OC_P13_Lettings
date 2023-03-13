import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_view_code():
    """Check if the view is accessible"""
    client = Client()
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_view_title():
    """Check if the title is OK"""
    client = Client()
    response = client.get(reverse('profiles:index'))
    assert "Profiles" in str(response.content)
