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

def NewFaveMeowPics(request):
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        form.save
        return HttpResponseRedirect('/fave_meow_pics')

class FavoriteForm(forms.ModelForm):
# class FavoriteForm(forms.Form):
    class Meta:
        model = FavoriteCatPic
        fields = ['url']
        # widgets = {'url': forms.HiddenInput()}
        # url = forms.HiddenInput()
        # hidden_field = forms.CharField()
