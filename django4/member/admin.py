from django.contrib import admin
from .models import Question
# Register your models here.
# admin페이지에서 관리할 model 등록

# admin 페이지에서 Question으로 만든 table을 manage하기 위해 register함
admin.site.register(Question)