from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/main/img/users/%Y/%m/%d/', verbose_name='Изображение', blank=True, null=True)
    bdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    coffee_address = models.TextField(blank=False, null=True)
    number = models.CharField(max_length=11, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, blank=True, null=True)

    def __unicode__(self):
        return self.user
 
    class Meta:
       verbose_name = 'Профиль'
       verbose_name_plural = 'Профили'


class Role(models.Model):
    role = models.PositiveIntegerField(primary_key=True)
    role_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class News(models.Model):
    topic = models.CharField(max_length=255, verbose_name='Заголовок')
    news_text = models.TextField(blank=True, verbose_name='Текст новости')
    photo = models.ImageField(upload_to="static/main/img/news/%Y/%m/%d/", verbose_name='Изображение')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True, verbose_name='Роль')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.topic
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

#class RoleCourses(models.Model):
#    kurs = models.PositiveIntegerField(primary_key=True)
#    kurs_name = models.CharField(max_length=100)
 #   role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

class Course(models.Model):
    course = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100, default='Title')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
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


class CategoryProduct(models.Model):
    category = models.PositiveIntegerField("Номер категории продукта", primary_key=True) 
    name = models.CharField("Имя категории", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фотография", upload_to="main/img/%Y/%m/%d/")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

class AboutProduct(models.Model):
    'id то есть primary key будет создан автоматически'
    food_name = models.CharField(verbose_name="Продукт", max_length=150)
    price = models.PositiveIntegerField(verbose_name="Цена", help_text = "указывать сумму в рублях")
    squirrels = models.PositiveIntegerField(verbose_name="Белки")
    fats = models.PositiveIntegerField(verbose_name="Жиры")
    carbohydrates = models.PositiveIntegerField(verbose_name="Каброгидраты")
    description_of_food = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="static/main/img/aboutproduct/%Y/%m/%d/", blank=True)
    cat = models.ForeignKey('CategoryProduct', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.food_name
    
    class Meta:
        verbose_name = 'О продукте'
        verbose_name_plural = 'О продуктах'


