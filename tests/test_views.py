from django.test import Client, TestCase
from django.urls import reverse

from meow_pics_app.views import HomePageView

client = Client()

class HomePageTest(TestCase):
    def test_root_url_renders_home_page(self):
        home_page = client.get(reverse('home'))

        self.assertTrue(home_page.status_code, 200)
        self.assertTemplateUsed(home_page, 'home.html')
