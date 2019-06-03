"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('base1', views.base1, name='base1'),
    path('base2', views.base2, name='base2'),
    path('sing', views.sing, name='sing'),
    path('sing1', views.sing1, name='sing1'),
    path('sing2', views.sing2, name='sing2'),
    path('sing3', views.sing3, name='sing3'),
    path('sing4', views.sing4, name='sing4'),
    path('sing5', views.sing5, name='sing5'),
    path('sing6/<int:id>', views.sing6, name='sing6'),
    path('sing7/<str:id>', views.sing7, name='sing7'),
    path('sing8/<str:id>', views.sing8, name='sing8'),
    path('sing9/<str:id>', views.sing9, name='sing9'),

]


