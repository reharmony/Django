from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 컨트롤러 역할하는 파일: views
# 함수를 호출하는 방식 / 클래스를 호출하는 방식 총 2가지가 있음

def start(request):
    return HttpResponse("<a href=/member/>member 첫 페이지로 이동</a>")

def index(request):
    # 요청에 대한 처리 내용...
    # return render(request, "member/hi.html")
    # return HttpResponse("나는 첫 페이지입니다.")
    return HttpResponse("<a href=hi>hi.html로 연결하기</a><br>\
                        <a href=hi2>hi2.html로 연결하기</a>")

def hi(request):
    context = {
        'title' : 'python',
        'name' : 'park',
        'age' : 100
    }
    return render(request, "member/hi.html", context) # context: 전달할 데이터 넣는 자리 (딕셔너리 형태로)

def hi2(request):
    return render(request, "member/hi2.html", {"product":"shoes", "price":20000})

def hi3(request):
    post = request.POST
    print(post)
    context = {
        "post" : post
    }
    return render(request, "member/hi3.html", context)

def hi4(request):
    post = request.POST
    print(post)
    context = {
        "post" : post
    }
    return render(request, "member/hi4.html", context)