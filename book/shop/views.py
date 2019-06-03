from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Count
import datetime
# Create your views here.

# 첫 페이지
def index(request):
    return HttpResponse('<a href=shop/readall>도서 관리 시스템으로 이동</a>')

# 도서 전체 목록
def readall(request):
    book_count = Product.objects.order_by('-id').filter(valid = True).count() # 유효한 항목 카운트
    print(book_count)
    total_page = int((book_count / 3) + 1) # 전체 페이지 수 구하기 (페이지당 3개 기준)
    print(total_page)
    page = 1
    offset = (page - 1) * 3 # 건너뛸 항목 수
    book_select = Product.objects.order_by('-id').filter(valid=True)[offset:offset+3] # 현재 페이지에 보여줄 항목만 select
    book_list = []
    for x in book_select:
        book_dic = {}
        book_dic['id'] = x.id
        book_dic['title'] = x.title
        book_dic['price'] = x.price
        book_dic['reg_date'] = str(x.reg_date)[0:16]
        book_dic['view_count'] = x.view_count
        book_list.append(book_dic)
    context = {
        'book_list' : book_list
    }
    return render(request, 'shop/readall.html', context)

# 도서 검색 화면
def readsearch(request):
    post = request.GET
    title = post['search']
    book_select = Product.objects.order_by('-id').filter(title__icontains = title, valid = True) # __icontains: SQL문의 %LIKE%
    book_list = []
    for x in book_select:
        book_dic = {}
        book_dic['id'] = x.id
        book_dic['title'] = x.title
        book_dic['price'] = x.price
        book_dic['reg_date'] = str(x.reg_date)[0:16]
        book_dic['view_count'] = x.view_count
        book_list.append(book_dic)
    context = {
        'book_list' : book_list
    }
    return render(request, 'shop/readsearch.html', context)

# 도서 정보 상세 보기
def read(request, id):
    book_select = Product.objects.filter(id=id)
    book_content = str(book_select[0]).split(',')
    reg_date = book_content[5]
    view_count = book_content[6]
    view_update = Product.objects.filter(id=id).update(view_count = int(view_count) + 1)
    context = {
        'book' : book_select[0],
        'reg_date' : reg_date
    }
    return render(request, 'shop/read.html', context)

# 도서 정보 등록
def create(request):
    return render(request, 'shop/create.html')

# 도서 정보 등록 처리
def createAction(request):
    post = request.POST
    title = post['title'],
    author = post['author'],
    pub_date = post['pub_date'],
    price = post['price'],
    img_url = post['img_url'],
    reg_date = datetime.date.today()
    create_new = Product(title = title[0],
                         author = author[0],
                         pub_date = pub_date[0],
                         price = price[0],
                         img_url = img_url[0],
                         reg_date = reg_date)
    create_new.save()
    context = {
        'title' : title[0],
        'author' : author[0],
        'pub_date' : pub_date[0],
        'price' : price[0] + '원',
        'img_url' : img_url[0],
        'reg_date' : reg_date.strftime('%Y-%m-%d')
    }
    return render(request, 'shop/createAction.html', context)

# 도서 정보 수정
def update(request, id):
    book_select = Product.objects.filter(id = id)
    book_content = str(book_select[0]).split(',')
    reg_date = book_content[5]
    print('book_select[0]:', book_select[0])
    context = {
        'id' : id,
        'book' : book_select[0],
        'reg_date' : reg_date
    }
    return render(request, 'shop/update.html', context)

# 도서 정보 수정 처리
def updateAction(request, id):
    post = request.POST
    title = post['title'],
    author = post['author'],
    pub_date = post['pub_date'],
    price = post['price'],
    img_url = post['img_url'],
    reg_date = datetime.date.today()
    update_book = Product.objects.filter(id = id).update(title = title[0])
    update_book = Product.objects.filter(id = id).update(author = author[0])
    update_book = Product.objects.filter(id = id).update(pub_date = pub_date[0])
    update_book = Product.objects.filter(id = id).update(price = price[0])
    update_book = Product.objects.filter(id = id).update(img_url = img_url[0])
    update_book = Product.objects.filter(id = id).update(reg_date = reg_date)
    return render(request, 'shop/updateAction.html')

# 도서 정보 삭제 처리
def delete(request, id):
    book_delete = Product.objects.filter(id = id).update(valid = False)
    return render(request, 'shop/delete.html')