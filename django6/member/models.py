from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 2048)
    name = models.CharField(max_length = 10)
    write_time = models.DateTimeField('write_time')
    view_count = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id) + "," + self.title + "," + self.content + "," + self.name + "," + str(self.write_time) + "," + str(self.view_count)