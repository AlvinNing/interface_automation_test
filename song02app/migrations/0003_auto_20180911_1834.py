# Generated by Django 2.1 on 2018-09-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song02app', '0002_auto_20180911_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='项目名称',
            field=models.CharField(max_length=20),
        ),
    ]
