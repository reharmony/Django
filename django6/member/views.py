from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.utils import timezone
# Create your views here.

# 메인화면
def index(request):
    return HttpResponse('<a href=member/base>base 화면으로 연결</a><br>' +
                        '<a href=member/sing>sing 화면으로 연결</a>')

def base(request):
    return render(request, 'member/base.html')

def base1(request):
    return render(request, 'member/base1.html')

def base2(request):
    return render(request, 'member/base2.html')

def sing(request):
    return render(request, 'member/sing.html')

def sing1(request):
    return render(request, 'member/sing1.html')

def sing2(request):
    return render(request, 'member/sing2.html')

# 문의게시판 메인
def sing3(request):
    board_list = Board.objects.order_by('-id') # 글목록 전체 아이디 기준 내림차순으로 불러오기
    board_result = [] # 최종적으로 보낼 결과값 저장할 리스트
    for x in board_list: # 게시글 정보 글 하나씩 꺼내기
        board_dic = {} # 각 항목을 저장할 딕셔너리
        board_dic['id']=x.id # 게시물 번호
        board_dic['title']=x.title # 제목
        board_dic['content']=x.content # 내용
        board_dic['name']=x.name # 작성자
        board_dic['write_time']=x.write_time.strftime("%Y-%m-%d %H:%M") # 작성시간
        board_dic['view_count']=x.view_count # 조회수
        board_result.append(board_dic) # 딕셔너리에 저장된 항목들을 리스트로 저장
    print(board_result)
    context = {
        "board_result" : board_result,
    }
    return render(request, 'member/sing3.html', context)

# 문의게시판 글쓰기 화면
def sing4(request):
    return render(request, 'member/sing4.html')

# 문의게시판 작성글 작성직후 확인 화면
def sing5(request):
    post = request.POST # 글쓰기 화면에서 작성한 내용 받아오기
    print(post)
    write_new = Board(title = post['title'], content = post['content'], name = post['name'], write_time = timezone.now()) # DB에 insert
    write_new.save() # commit
    context = {
        'post' :  post,
        'write_time' : timezone.now().strftime("%Y-%m-%d %H:%M")
    }
    return render(request, 'member/sing5.html', context)

# 게시판에서 글 제목 클릭시 글 내용 보여주는 화면
def sing6(request,id):
    board_num = Board.objects.filter(id=id) # 클릭한 글 글번호로 DB에서 select
    board_record = str(board_num[0]).split(",") # string형태로 받아와서 ,로 각 항목 분리
    print(board_record)
    context = {
        'id' : board_record[0],
        'title' : board_record[1],
        'content' : board_record[2],
        'name' : board_record[3],
        'write_time' : board_record[4][0:16],
        'view_count' : int(board_record[5])+1
    }
    Board.objects.filter(id = id).update(view_count=int(board_record[5])+1) # 조회수 1증가 DB에 update
    return render(request, 'member/sing6.html', context)

# 글 삭제 처리하는 페이지
def sing7(request, id):
    delete_board = Board.objects.filter(id = id).delete() # DB에서 delete
    return render(request, 'member/sing7.html')

# 글 수정 하는 화면
def sing8(request, id):
    print(id)
    board_num = Board.objects.filter(id = id) # DB에서 select
    board_record = str(board_num[0]).split(",") # string형태로 받아와서 ,로 각 항목 분리
    print(board_record)
    context = {
        'id' : board_record[0],
        'title' : board_record[1],
        'content' : board_record[2],
        'name' : board_record[3],
        'write_time' : board_record[4][0:16]
    }
    return render(request, 'member/sing8.html', context)

# 글 수정 처리하는 페이지
def sing9(request, id):
    post = request.POST # 글 수정화면에서 받아온 정보
    print(post)
    update_board = Board.objects.filter(id = id).update(title=post['title']) # 제목 DB에 update
    update_board = Board.objects.filter(id = id).update(content=post['content']) # 내용 DB에 update
    update_board = Board.objects.filter(id = id).update(name=post['name']) # 작성자 DB에 update
    update_board = Board.objects.filter(id = id).update(write_time=timezone.now()) # 수정시간 DB에 update
    return render(request, 'member/sing9.html')