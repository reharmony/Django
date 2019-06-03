from django.db import models

# Create your models here.
# 테이블을 정의하는 파일
# 자동으로 sql문으로 변환해서 DB와 통신 (ORM)
# ORM: Object Relational Mapping -> 객체(클래스)와 RDB를 연결해줌
# class 1개가 테이블 1개
# 변수 1개가 column 1개

class Question(models.Model): # models의 속성 상속 받음
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published.')

    def __str__(self):
        return '{} {}'.format(self.question_text, self.pub_date)


