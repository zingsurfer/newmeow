"""tellerai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from meow_pics_app import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('fave_meow_pics',
          views.FaveMeowPicsIndex.as_view(),
          name='fave_meow_pics'),
    path('new_fave_meow_pics',
          views.NewFaveMeowPics.as_view(),
          name='new_fave_meow_pics')
]
