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
urlpatterns = [ # 내가 사용할 URL들 등록하기
    path('', views.index, name='index2'),  # 공백의 요청의 들어왔을 때 views파일 안의 index함수 실행, name은 안 넣어도 무방
    path('hi', views.hi, name='hi'),
    path('tomember', views.tomember, name='tomember'),

]
