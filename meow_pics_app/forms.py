from django import forms
from django.forms import ModelForm
from .models import FavoriteCatPic

class FavoriteCatPicForm(ModelForm):
    required_css_class='required'
    class Meta:
        model = FavoriteCatPic
        fields = ['url']
