from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 20)
    pub_date = models.CharField(max_length = 15)
    price = models.CharField(max_length = 10)
    img_url = models.CharField(max_length = 100)
    reg_date = models.DateField('registered date')
    view_count = models.IntegerField(default = 0)
    valid = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.pk)])

    def __str__(self):
        return self.title + ", " + self.author + ", " + str(self.pub_date) + ", " + self.price + ", " + self.img_url + ", " + str(self.reg_date) + ", " + str(self.view_count) + ", " + str(self.valid)