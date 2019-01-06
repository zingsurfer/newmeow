import requests
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request):
        return render(request, 'home.html')
