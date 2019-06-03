# Generated by Django 2.2.1 on 2019-05-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('pub_date', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
                ('img_url', models.CharField(max_length=100)),
                ('reg_date', models.DateField(verbose_name='registered date')),
            ],
        ),
    ]