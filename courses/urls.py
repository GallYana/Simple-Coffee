from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.show_course, name='course'),
    path('module/<int:module_id>/', views.show_module, name='module'),
    path('lection/<int:lection_id>/', views.show_lection, name='lection'),
]