# Generated by Django 3.1.7 on 2021-05-20 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_delete_lection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lection',
            fields=[
                ('lection', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(default='Topic of lection', max_length=100)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.module')),
            ],
        ),
    ]
