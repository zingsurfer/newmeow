import os
import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .services.pic_generator import PicGenerator

class HomePageView(TemplateView):
    def get(self, request):
        # api_url = 'https://api.thecatapi.com/v1/images/search'
        # headers = {'x-api-key': f'{os.environ.get("CAT_KEY")}'}
        # response = requests.get(api_url, headers=headers)
        # data = response.json()
        # pic_url = data[0]["url"]
        random_cat_pic = PicGenerator.random
        return render(request, 'home.html',{'random_cat_pic':random_cat_pic})
