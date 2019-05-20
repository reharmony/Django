from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>상품 안내 메인 페이지입니다.</h1><br><br>\
                        <h2><a href=/basket>장바구니 메인페이지로 이동</a></h2><br><br>\
                        <a href=detail>상품 상세페이지</a><br>\
                        <a href=list>상품 목록페이지</a><br>\
                        <a href=sale>특별할인 페이지</a>\
                        <body bgcolor="yellow">')

def detail(request):
    return render(request,'product/productDetail.html')

def list(request):
    return render(request,'product/productList.html')

def sale(requset):
    return HttpResponse("특별할인 페이지입니다.<br>\
                        <a href=/product>상품 안내 메인으로 돌아가기</a> <body bgcolor='yellow'>")