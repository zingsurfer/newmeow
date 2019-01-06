import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .services.pic_generator import PicGenerator

class HomePageView(TemplateView):
    def get(self, request):
        random_cat_pic = PicGenerator.random

        return render(request, 'home.html',{'random_cat_pic':random_cat_pic})
