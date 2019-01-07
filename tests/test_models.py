from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from meow_pics_app.models import FavoriteCatPic

class FavoriteCatPicTest(TestCase):
    def create_favorite_cat_pic(self, url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYQo_3zC1FpgMmtbD0IDEVKiCMZ8H3SfbtBTOn42O8_fIj4fe8xQ"):
        return FavoriteCatPic.objects.create(url=url, created_at=timezone.now(), updated_at=timezone.now())

    def test_favorite_cat_pic_creation(self):
        favorite_cat_pic = self.create_favorite_cat_pic()
        self.assertTrue(isinstance(favorite_cat_pic, FavoriteCatPic))
