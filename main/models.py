from django.db import models
from django.utils import timezone
from django.conf import settings

# class User(models.Model):
#     user = models.CharField(max_length=254, default='name')
#     bdate = models.DateField(auto_now=False, auto_now_add=False)
#     coffee_address = models.TextField(blank=False)
#     number = models.CharField(max_length=11, blank=True)
#     email = models.EmailField(max_length=254)
#     login = models.TextField()
#     password = models.TextField()

# class Role(models.Model):
#     role = models.PositiveIntegerField(primary_key=True)
#     role_name = models.CharField(max_length=100)
#     user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)

# class News(models.Model):
#     topic = models.CharField(max_length=255)
#     news_text = models.TextField(blank=True)
#     photo = models.ImageField(upload_to="static/main/img/news/%Y/%m/%d/", blank=True)
#     role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.topic

# class RoleCourses(models.Model):
#     kurs = models.PositiveIntegerField(primary_key=True)
#     kurs_name = models.CharField(max_length=100)
#     role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
#     kurs = models.OneToOneField(RoleCourses, on_delete = models.CASCADE, primary_key = True)

class AboutProduct(models.Model):
    'id то есть primary key будет создан автоматически'
    food_name = models.CharField(verbose_name="Продукт", max_length=150)
    price = models.PositiveIntegerField(verbose_name="Цена", help_text = "указывать сумму в рублях")
    squirrels = models.PositiveIntegerField(verbose_name="Белки")
    fats = models.PositiveIntegerField(verbose_name="Жиры")
    carbohydrates = models.PositiveIntegerField(verbose_name="Каброгидраты")
    description_of_food = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="static/main/img/aboutproduct/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.food_name
    
    class Meta:
        verbose_name = 'О продукте'
        verbose_name_plural = 'О продуктах'
