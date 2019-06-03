from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Photo(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_photos') # 외래키 CASCADE
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', default = 'photos/no_image.png') # 파일 업로드
    text = models.TextField() # 긴 글?
    created = models.DateTimeField(auto_now_add = True) # auto_now_add: 최초 레코드 생성 일시 고정
    updated = models.DateTimeField(auto_now = True) # auto_now: save할 때마다 수정 일시 업데이트

    class Meta: # 클래스 안의 클래스는 많이 사용되는 방법은 아님. 상위 클래스에 종속적.
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime('%Y-%m-%d %H:%M')

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])
