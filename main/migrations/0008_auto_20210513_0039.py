# Generated by Django 3.1.7 on 2021-05-12 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210513_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]