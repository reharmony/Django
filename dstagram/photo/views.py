from django.shortcuts import *
from django.views.generic import *
from .models import Photo

# Create your views here.

# 전체 검색: 함수
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

# 사진 업로드
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form): # 로그인 된 유저인지 확인
        form.instance.author_id = self.request.user.id
        if form.is_valid(): # 로그인 중인 경우
            form.instance.save() # 사진 업로드 commit
            return redirect('/') # 완료 후 메인 페이지로 돌아감
        else: # 로그아웃 상태인 경우
            return self.render_to_response({'form':form}) # 어디로 돌아가누

# 사진 삭제
class PhotoDelete(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

# 사진 변경
class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
