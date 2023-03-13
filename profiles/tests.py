import pytest
from django.test import TestCase
from django.urls import reverse

class ProfilesTest(TestCase):
    def test_view_code(self):
        """Check if the view is accessible"""
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_view_title(self):
        """Check if the title is OK"""
        response = self.client.get(reverse('profiles:index'))
        assert "Profiles" in str(response.content)
