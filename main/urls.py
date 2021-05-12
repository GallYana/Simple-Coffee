from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.about, name='menu'),
    path('library/', views.library, name='library'),
    path('personalaccount/', views.account, name='personalaccount'),
    path('news/', views.post_list, name='post'),
    path('barista/', views.barista, name='bar'),
    path('register/', views.RegisterFormView.as_view(), name="register"),
    path('login/', views.LoginFormView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]