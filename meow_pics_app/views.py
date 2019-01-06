import os
import requests
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request):
        api_url = 'https://api.thecatapi.com/v1/images/search'
        headers = {'x-api-key': f'{os.environ.get("CAT_KEY")}'}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        pic_url = data[0]["url"]

        return render(request, 'home.html',{'pic':pic_url})
