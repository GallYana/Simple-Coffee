# Generated by Django 3.1.7 on 2021-05-09 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210509_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='role',
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rolecourses',
            name='role',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='RoleCourses',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
