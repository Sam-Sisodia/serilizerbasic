from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.userdata),
    path('post/',views.userpost),

    path('course/',views.course.as_view()),
    path('course/<int:pk>',views.coursedetails.as_view()),

    

]