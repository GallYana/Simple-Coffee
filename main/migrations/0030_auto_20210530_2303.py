# Generated by Django 3.2.3 on 2021-05-30 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_lection_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_name',
            field=models.CharField(default='Title of module', max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='module',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.course', verbose_name='Курс'),
        ),
    ]