from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Board
from django.views.generic import *
from django.urls import reverse_lazy


# Create your views here.


def index(reqeust):
    return HttpResponse('<a href=member/readall>게시판 입장</a>')


class Readall(ListView):
    model = Board
    template_name = 'member/readall.html'
    paginate_by = 5

class Read(DetailView):
    model = Board
    template_name = 'member/read.html'

class Create(CreateView):
    model = Board
    fields = ['name', 'title', 'content', 'write_time']
    success_url = reverse_lazy('readall')
    template_name = 'member/create.html'

class Update(UpdateView):
    model = Board
    fields = ['name', 'title', 'content', 'write_time']
    success_url = reverse_lazy('readall')
    template_name = 'member/update.html'

class Delete(DeleteView):
    model = Board
    success_url = reverse_lazy('readall')
    template_name = 'member/delete.html'