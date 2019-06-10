from django.shortcuts import render, get_object_or_404

from cart.forms import AddProductForm
from .models import *

# Create your views here.
# 모든 카테고리 출력
# 해당 카테고리 클릭하면 출력
def product_in_category(request, category_slug=None): # category_slug값이 있으면 값을 받고, 없으면 None을 default값으로 지정
    # DB검색 결과를 템플릿에 넘겨줌
    # map형태로 만들어서 넘겨줌
    current_category = None # 현재 선택된 카테고리

    # category없이 전체 출력
    categories = Category.objects.all() # 카테고리 전체 목록 select
    products = Product.objects.filter(available_display = True) # 모든 카테고리의 상품 목록 select

    # category에 해당하는 것만 출력
    if category_slug: # category_slug에
        current_category = get_object_or_404(Category, slug = category_slug) # 값이 있으면 가져오고 없으면 404처리해주는 함수
        products = products.filter(category = current_category) # 선택된 카테고리에 해당하는 상품만 select

    return render(request, 'shop/list.html', {
        'current_category' : current_category,
        'products' : products,
        'categories' : categories})


# 제품 상세페이지 출력
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial = {'quantity':1})

    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart})

