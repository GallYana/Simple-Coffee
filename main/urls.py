from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.about, name='menu'),
    path('library/', views.library, name='library'),
    #path('account/', views.p_account, name='personalaccount'),
    path('news/', views.post_list, name='post'),
    path('barista/', views.barista, name='bar'),
    path('registration/', views.user_registration, name="registration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]