# Generated by Django 3.2.3 on 2021-05-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20210530_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='order_course',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер в курсе'),
        ),
    ]
