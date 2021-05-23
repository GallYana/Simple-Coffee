# Generated by Django 3.1.7 on 2021-05-23 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20210522_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(blank=True, verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='static/main/img/news/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.role', verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/main/img/users/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
