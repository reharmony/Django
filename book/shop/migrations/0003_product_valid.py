# Generated by Django 2.2.1 on 2019-05-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]