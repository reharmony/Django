# Generated by Django 2.2.1 on 2019-05-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
