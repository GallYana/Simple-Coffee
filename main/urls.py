from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('library/', views.library, name='library'),
    path('account/', views.p_account, name='account'),
    path('course/<int:course_id>/', views.show_course, name='course'),
    path('module/<int:module_id>/', views.show_module, name='module'),
    path('lection/<int:lection_id>/', views.show_lection, name='lection'),
    path('registration/', views.user_registration, name="registration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]