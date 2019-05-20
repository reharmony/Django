from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 클라이언트의 요청에 응답하는 함수
def index(request):
    return HttpResponse("ok...")

def index2(request):
    # return HttpResponse("i am a python programmer.")
    return HttpResponse("<a href=index3>나의 세번째 페이지로 연결</a>") # 바로 하이퍼링크 구현됨

def index3(request):
    # return HttpResponse("i am index3 page...")
    return HttpResponse("<a href=index4>나의 네번째 페이지로 연결</a>")

def index4(request):
    name = "자동차"
    return HttpResponse("<a href=index5/" + name + ">검색할 단어 전달 페이지로!</a>")

def index5(request, name):
    return HttpResponse("전달받은 값은: " + name + "<br>" +
                        "<a href=/member/index2>인덱스 2페이지로</a>"
                        )

def welcome(request):
    return render(request, 'member/welcome.html') # render로 파일호출, 경로는 templates 아래부터 작성

def tobbs(request):
    return HttpResponse("<a href=/bbs/hi>bbs의 hi로 연결</a>") # href를 /로 시작하면 port번호 뒤에 붙여줌