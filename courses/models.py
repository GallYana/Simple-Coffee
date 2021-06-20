from django.db import models
from django.urls import reverse
from main.models import Role

class Course(models.Model):
    course = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100, default='Title')
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course', kwargs={'course_id': self.pk})
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
class Module(models.Model): 
    module = models.AutoField(primary_key=True, verbose_name='ID')
    parent = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name='Курс') 
    module_name = models.CharField(max_length=100, default='Title of module', verbose_name='Название')
    order_course = models.PositiveIntegerField(verbose_name='Номер в курсе', null=True, blank=True)
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    def __str__(self):
        return self.module_name

    def get_absolute_url(self):
        return reverse('module', kwargs={'module_id': self.pk})

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

class Lection(models.Model):
    lection = models.AutoField(primary_key=True, verbose_name='ID')
    topic = models.CharField(max_length=100, default='Topic of lection', verbose_name='Заголовок')
    parent = models.ForeignKey('Module', on_delete=models.PROTECT, null=True, verbose_name='Модуль') 
    order_lection = models.PositiveIntegerField(verbose_name='Номер в модуле', null=True, blank=True)

    def __str__(self):
        return self.topic
    
    def get_absolute_url(self):
        return reverse('lection', kwargs={'lection_id': self.pk})

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

class LectionContent(models.Model):
    parent = models.ForeignKey('Lection', on_delete=models.PROTECT, null=True, verbose_name='Лекция') 
    content = models.TextField(verbose_name="Содержание", null=True)

    def __str__(self):
        return self.parent.topic

    class Meta:
        verbose_name = 'Контент лекции'
        verbose_name_plural = 'Контенты лекций'
