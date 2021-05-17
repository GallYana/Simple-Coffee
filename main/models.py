from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/main/img/users/%Y/%m/%d/', verbose_name='Изображение')
    bdate = models.DateField(auto_now=False, auto_now_add=False, null=True)
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

class News(models.Model):
    topic = models.CharField(max_length=255)
    news_text = models.TextField(blank=True)
    photo = models.ImageField(upload_to="static/main/img/news/%Y/%m/%d/")
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.topic

class RoleCourses(models.Model):
    kurs = models.PositiveIntegerField(primary_key=True)
    kurs_name = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    kurs = models.OneToOneField(RoleCourses, on_delete = models.CASCADE, primary_key = True)

class CategoryProduct(models.Model):
    category = models.PositiveIntegerField("Номер категории продукта", primary_key=True) 
    name = models.CharField("Имя категории", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фотография", upload_to="main/img/%Y/%m/%d/")

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


