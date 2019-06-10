from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin): # 관리자모드 화면 설정하는 class 상속 받음
    list_display = ['name', 'slug'] # 보여줄 항목 지정
    prepopulated_fields = {'slug':('name',)} # 자동입력?

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['available_display', 'created', 'updated', 'category'] # 관리자 페이지에서의 정렬기준 지정
    list_editable = ['price', 'stock', 'available_display', 'available_order'] # 관리자 페이지 목록화면에서 수정가능한 항목 지정(각 항목별 세부설정화면에서는 전부 수정가능)


admin.site.register(Category, CategoryAdmin) # 두번째 항목은 화면을 담당하는 class 지정
admin.site.register(Product, ProductAdmin) # 두번째 항목은 화면을 담당하는 class 지정
