from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.about, name='menu'),
    path('library/', views.library, name='library'),
    path('personalaccount/', views.account, name='personalaccount'),
    path('news/', views.post_list, name='post'),
]