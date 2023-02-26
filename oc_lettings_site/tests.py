from django.test import Client
from django.urls import reverse


def test_view_code():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200

def test_view_title():
    client = Client()
    response = client.get(reverse('index'))   
    assert "Welcome to Holiday Homes" in str(response.content)