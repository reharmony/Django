from django.shortcuts import render
from django.http import HttpResponse
from . models import Test, Question
from django.views.generic.list import ListView
from django.views.generic.edit import *
from django.views.generic.detail import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse('<a href=member/create>Create(CreateView)</a><br>'+
                        '<a href=member/read>Read(DetailView)</a><br>'+
                        '<a href=member/readall>ReadAll(ListView)</a><br>'+
                        '<a href=member/update>Update(UpdateView)</a><br>'+
                        '<a href=member/delete>Delete(DeleteView)</a><br><hr>'+
                        '<a href=member/test1>Test1(기본View)</a><br>'+
                        '<a href=member/test2>Test2(TemplateView)</a><br>'+
                        '<a href=member/test3>Test3(RedirectView)</a><br>'+
                        '<a href=member/test4>Test4(DetailView)</a><br>'+
                        '<a href=member/test5>Test5(ListView)</a><br>'+
                        '<a href=member/test6>Test6(ListView)</a><br>'+
                        '<a href=member/test7>Test7(ListView)</a><br>'+
                        '<a href=member/test8>Test8(ListView)</a><br>'+
                        '<a href=admin>Admin</a><br>')

class Create(CreateView):
    model = Test
    fields = ['name', 'tel', 'addr']
    success_url = reverse_lazy('readall')
    template_name = 'member/create.html'


class Read(DeleteView):
    model = Test
    template_name = 'member/read.html'

class Readall(ListView):
    model = Test
    template_name = 'member/readall.html'

class Update(UpdateView):
    model = Test
    fields = ['name', 'tel', 'addr']
    success_url = reverse_lazy('readall')
    template_name = 'member/update.html'

class Delete(DeleteView):
    model = Test
    success_url = reverse_lazy('readall')
    template_name = 'member/delete.html'















class Test1(View): # View 클래스에서 상속받은것
    def get(self, request):
        return HttpResponse("hello class view..")

class Test2(TemplateView): # TemplateView에서 상속 받은 것
    template_name = 'member/home.html' # 오버라이드이므로 변수명 변경하면X
    # template_name_suffix = '_home'

class Test3(RedirectView): # RedirectView에서 상속 받은 것
    url  = 'http://www.naver.com'

class Test4(DetailView): # DB에 PK가 꼭 필요
    model = Test
    template_name = 'member/test_detail.html'

class Test5(ListView):
    model = Test
    template_name = 'member/test_list.html'

class Test6(ListView):
    model = Test
    template_name = 'member/test_list.html'

class Test7(ListView):
    model = Test
    template_name = 'member/test_list.html'

class Test8(CreateView):
    model = Test
    # 폼으로 만들 값을 fields로 설정
    fields = ['name', 'tel', 'addr'] # Model과 똑같이 지정해야 함
    success_url = reverse_lazy('test5') # lazy안은 urls의 name을 지정
    # template_name_suffix = '_create'
    template_name = 'member/test_create.html'

class Admin(ListView):
    model = Test
    template_name = 'member/test_list.html'