from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("BBS Ok...")

def hi(request):
    return render(request, 'bbs/hi.html')

def tomember(request):
    return HttpResponse("<a href=/member/welcome>member의 welcome페이지로 이동</a>" )