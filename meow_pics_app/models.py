from django.db import models

class FavoriteCatPic(models.Model):
    url = models.CharField(max_length=200)
