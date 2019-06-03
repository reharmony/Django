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
    path('create/', views.Create.as_view(), name='create'),
    path('read/<int:pk>', views.Read.as_view(), name='read'),
    path('readall/', views.Readall.as_view(), name='readall'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('test1/', views.Test1.as_view(), name='test1'),
    path('test2/', views.Test2.as_view(), name='test2'),
    path('test3/', views.Test3.as_view(), name='test3'),
    path('test4/<int:pk>', views.Test4.as_view(), name='test4'),
    path('test5/', views.Test5.as_view(), name='test5'),
    path('test6/<int:pk>', views.Test6.as_view(), name='test6'),
    path('test7/<int:pk>', views.Test7.as_view(), name='test7'),
    path('test8/', views.Test8.as_view(), name='test8'),
]

