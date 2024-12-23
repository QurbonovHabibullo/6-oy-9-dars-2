from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('courses/create/', views.create_course, name='create_course'),  
    path('course/<int:course_id>/lesson/create/', views.create_lesson, name='create_lesson'),
]
