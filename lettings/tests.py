from django.test import  TestCase
from django.urls import reverse

class LettingsTest(TestCase):
    def test_view_code(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200

    def test_view_title(self):
        response = self.client.get(reverse('lettings:index'))
        assert "Lettings" in str(response.content)
