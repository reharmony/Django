from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True)
    meta_description = models.TextField(blank = True)
    slug = models.SlugField(max_length = 200, unique = True, db_index = True, allow_unicode=True) # 언더바가 들어가는 형태

    class Meta: # 이 클래스 밖에선 쓸 수 없는 inner클래스?
        ordering = ['name']
        verbose_name = 'category' # 단수형 (관리자 모드에서 사용)
        verbose_name_plural = 'categories' # 복수형 (관리자 모드에서 사용)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args = [self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, related_name = 'products')
    name = models.CharField(max_length = 200, db_index = True)
    slug =  models.SlugField(max_length = 200, db_index = True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True)
    description = models.TextField(blank = True) # blank: valid함수가 무시하게 만드는 함수
    meta_description = models.TextField(blank = True)

    price = models.DecimalField(max_digits = 10, decimal_places = 2) # 10진수 필드, decimal_places: 소수점 자리수
    stock = models.PositiveIntegerField() # 양수값만 들어오는 필드

    available_display = models.BooleanField('Display', default = True)
    available_order = models.BooleanField('Order', default = True)

    created = models.DateTimeField(auto_now_add = True) # 최초생성날짜 유지
    updated = models.DateTimeField(auto_now = True) # 업데이트시 날짜 갱신

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']] # 외부대괄호: 문법, 내부대괄호: 리스트

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args = [self.id, self.slug])