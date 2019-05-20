from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>장바구니 메인 페이지입니다.</h1><br>\
                        <h2><a href=/product>상품 메인 페이지로 이동</a></h2><br><br>\
                        <a href=list>장바구니 목록으로 이동</a><br>\
                        <a href=cancel>장바구니 취소목록으로 이동</a>\
                        <body bgcolor="pink">')

def list(request):
    return render(request,'basket/basketList.html')

def cancel(request):
    return HttpResponse('취소목록: KURZWEIL PC2X\
                        <a href=/basket>장바구니 메인으로 돌아가기</a><body bgcolor="pink">')