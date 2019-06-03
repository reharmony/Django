from django.shortcuts import render
from django.http import HttpResponse
from .models import Question # 모델 import
# Create your views here.
def index(request):
    return HttpResponse("<a href=member/quiz>퀴즈 화면으로 연결</a><br>"+
                        "<a href=member/read>읽기 화면으로 연결</a><br>" +
                        "<a href=member/write>쓰기 화면으로 연결</a><br>" +
                        "<a href=member/bbs>게시판으로 연결</a>")

def quiz(request):
    quiz_list = Question.objects.order_by('-pub_date')[:5]
    context = {'quiz_list' : quiz_list}
    return render(request, "member/quiz.html", context)

def bbs(request):
    return render(request, "member/bbs.html")

def read(request):
    return render(request, "member/read.html")

def write(request):
    return render(request, "member/write.html")