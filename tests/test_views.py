from django.test import Client, TestCase
from django.urls import reverse

from meow_pics_app.views import HomePageView, FaveMeowPicsPageView

client = Client()

class HomePageTest(TestCase):
    def test_root_url_renders_home_page(self):
        home_page = client.get(reverse('home'))

        self.assertTrue(home_page.status_code, 200)
        self.assertTemplateUsed(home_page, 'home.html')

class FaveMeowPicsPageTest(TestCase):
    def test_favorite_meow_pics_url_renders_favorite_meow_pics_page(self):
        favorites_page = client.get(reverse('fave_meow_pics'))

        self.assertTrue(favorites_page.status_code, 200)
        self.assertTemplateUsed(favorites_page, 'fave_meow_pics/index.html')
