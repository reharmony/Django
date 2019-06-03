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
from django.urls import path
from .views import *
from .models import *
app_name = 'photo'
urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>', DetailView.as_view(model = Photo, template_name = 'photo/detail.html'), name='photo_detail'), # 짧은 뷰는 views.py 대신 여기에 넣어도 됨    path('upload/', PhotoUploadView.as_view(), name = 'photo_upload'),
    path('update/<int:pk>', PhotoUpdateView.as_view(), name = 'photo_update'),
    path('delete/<int:pk>', PhotoDelete.as_view(), name = 'photo_delete'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
]
