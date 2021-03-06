# Generated by Django 3.2.3 on 2021-05-24 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20210524_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(default='Title of module', max_length=100)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.course')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
            },
        ),
        migrations.CreateModel(
            name='Lection',
            fields=[
                ('lection', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(default='Topic of lection', max_length=100)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.module')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекции',
            },
        ),
    ]
