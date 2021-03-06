from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('library/', views.library, name='library'),
    path('account/', views.p_account, name='account'),
    path('account/edit', views.p_account_edit, name='account_edit'),
    path('registration/', views.user_registration, name="registration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]