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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ # 내가 사용할 URL들 등록하기
    path('admin/', admin.site.urls), # URL에 표시할 경로 / 실제 파일 경로
    path('member/', include('member.urls')),  # 보안을 위해 표시 경로와 실제 경로를 다르게 쓰는것이 일반적
    path('bbs/', include('bbs.urls')),  # bbs라는 app 안에 있는 urls.py 파일
]
