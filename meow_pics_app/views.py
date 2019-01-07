import requests
from django.shortcuts import render
from meow_pics_app.models import FavoriteCatPic
from django.views.generic import TemplateView, ListView
from .services.pic_generator import PicGenerator

class HomePageView(TemplateView):
    def get(self, request):
        random_cat_pic = PicGenerator.random

        return render(request, 'home.html',{'random_cat_pic':random_cat_pic})

class FaveMeowPicsIndex(ListView):
    model = FavoriteCatPic
    template_name = 'fave_meow_pics/index.html'

    def get_fave_meow_pics(self):
        fave_meow_pics = FavoriteCatPic.objects.all()

        return fave_meow_pics
