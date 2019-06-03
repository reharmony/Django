from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text + " " + str(self.pub_date)

class Person(models.Model):
    name = models.CharField(max_length = 200)
    tel = models.CharField(max_length = 200)
    addr = models.CharField(max_length = 200)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.tel, self.addr)