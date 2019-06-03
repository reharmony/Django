from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Person
# Create your views here.

def index(request):
    return HttpResponse('<a href=member/quiz>질문 화면으로</a><br>' +
                        '<a href=member/join>회원가입 화면으로</a>')

def quiz(request):
    # DB 검색결과를 받아와야 함
    quiz_list = Question.objects.order_by('id')[:5] # 역순은 '-id'
    # 받아온 검색결과를 딕셔너리 형태로 만들어줌
    context = {
        'quiz_list' : quiz_list,
    }
    # 템플릿으로 전송
    return render(request, 'member/quiz.html', context)

def quiz2(request, id):
    # DB 검색결과를 받아와야 함
    quiz_list = Question.objects.order_by('-pub_date')
    # 받아온 검색결과를 딕셔너리 형태로 만들어줌
    for x in quiz_list:
        if x.id == id:
            pub_date = str(x.pub_date)
            question_text = x.question_text
    context = {
        'id' : id,
        'pub_date' : pub_date,
        'question_text' : question_text
    }
    # 템플릿으로 전송
    return render(request, 'member/quiz2.html', context)

def join(request):
    return render(request, 'member/join.html')

def list(request):
    post = request.POST
    print(post)
    join_new = Person(name = post['name'], tel = post['tel'], addr = post['addr'])
    join_new.save()
    member_list = Person.objects.order_by('id')
    print(member_list)
    for x in member_list :
        id = x.id
        name = str(x.name)
        tel = x.tel
        addr = x.addr
    context = {
        "post" : post,
        "member_list" : member_list,
        "id" : id,
        "name" : name,
        "tel" : tel,
        "addr" : addr
    }
    return render(request, "member/list.html", context)
