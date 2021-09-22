# from django.conf.urls import url
from django.urls import path
from .views import delete_student, edit_student, register_student, student_profile
from.views import student_list
from.views import edit_student


# app_name='student'
urlpatterns=[
    path("register/", register_student,name="register_student"),
    path('list/',student_list,name="student_list"),
    path('profile/<int:id>/',student_profile,name="student_profile"),
    path('delete/<int:id>/',delete_student,name="delete_student"),
    path('edit/<int:id>/',edit_student,name="edit_student"),

]