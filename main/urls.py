from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.about, name='menu'),
    path('library/', views.library, name='library'),
    path('account/', views.p_account, name='account'),
    path('barista/', views.barista, name='bar'),
    path('barista/mod1', views.show_module, name='mod1'),
    path('registration/', views.user_registration, name="registration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]