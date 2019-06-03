from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length = 20)
    tel = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.pk)])

    def __str__(self):
        return self.name + ", " + self.tel + ", " + self.addr

class Board(models.Model):
    name = models.CharField(max_length = 20)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 2048)
    write_time = models.DateTimeField('date published')

    def get_absolute_url(self) :
        return reverse('detail', args = [str(self.pk)])

    def __str__(self):
        return self.name + ", " + self.title + ", " + self.content + ", " + str(self.write_time)