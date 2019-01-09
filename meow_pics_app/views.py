import requests
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponseRedirect

from meow_pics_app.models import FavoriteCatPic
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

class NewFaveMeowPics(CreateView):
    template_name = 'favorites_form.html'
    model = FavoriteCatPic
    fields = ['url']
    success_url = reverse_lazy('fave_meow_pics')

class FavoriteForm(forms.Form):
    class Meta:
        model = FavoriteCatPic
        fields = ('url')
