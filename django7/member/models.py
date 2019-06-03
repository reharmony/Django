from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text + str(self.pub_date)

class Test(models.Model):
    name = models.CharField(max_length = 200)
    tel = models.CharField(max_length = 200)
    addr = models.CharField(max_length = 200)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])

    def __str__(self):
        return self.name + ", " + self.tel + ", " + self.addr