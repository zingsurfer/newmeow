import requests
from django.shortcuts import render
from meow_pics_app.models import FavoriteCatPic
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from .services.pic_generator import PicGenerator
from django.forms import ModelForm, Form
from django import forms
from django.http import HttpResponseRedirect


class HomePageView(CreateView):
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
    template_name = 'home.html'
    model = FavoriteCatPic
    fields = ['url']
    success_url = reverse_lazy('fave_meow_pics')
    def get_url(self, request):
        # if self.request.method == 'POST':
        url = self.request.POST.get('url')
        new_fave_meow_pic =FavoriteCatPic.objects.create(url=url)
        return HttpResponseRedirect(reverse('fave_meow_pics'))

    # widgets = {'url': forms.HiddenInput()}

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        # return super(NewFaveMeowPics, self).form_valid(form)
        return HttpResponseRedirect(reverse('fave_meow_pics'))
    # "https://www.top13.net/wp-content/uploads/2015/10/perfectly-timed-cat-photos-funny-cover.jpg"
    # print("JUST BEFORE DEF")
    # def create_fave_meow_pics(request, url):
    #     print(request)
    #     print("CREATE FAVE MEOW PICS IS RUNNING")
    #     new_fave_meow_pic =FavoriteCatPic.objects.create(url=url)
    #     favorite_form = FavoriteForm(request.POST)
    #     # return redirect('/fave_meow_pics')
    #     return HttpResponseRedirect('fave_meow_pics')




class FavoriteForm(forms.Form):
    # class Meta:
        # model = FavoriteCatPic
        # fields = ['url']
        # url = forms.HiddenInput()
    # widgets = {'url': forms.HiddenInput()}
    hidden_field = forms.CharField()
