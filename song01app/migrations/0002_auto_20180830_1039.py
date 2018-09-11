# Generated by Django 2.1 on 2018-08-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song01app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='bug_num',
            field=models.IntegerField(blank=True, help_text='bug统计总数量'),
        ),
        migrations.AlterField(
            model_name='result',
            name='name',
            field=models.CharField(help_text='测试执行人', max_length=150),
        ),
        migrations.AlterField(
            model_name='result',
            name='version_num',
            field=models.PositiveIntegerField(help_text='版本号'),
        ),
    ]
