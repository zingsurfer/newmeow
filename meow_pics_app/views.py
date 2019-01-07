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
    def get(self, request):
        model = FavoriteCatPic
        # fave_pics = FavoriteCatPic.objects
        # return render(request, 'fave_meow_pics/index.html')
        template_name = 'fave_meow_pics/index.html'
        fave_pics = ["https://cdn2.thecatapi.com/images/265.jpg", "https://cdn2.thecatapi.com/images/123.jpg"]
        return render(request, template_name, {'fave_meow_pics':fave_pics})
