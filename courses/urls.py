
from django.urls import path
from .views import course_profile
from.views import delete_courses
from.views import edit_course
from .views import register_courses
from.views import course_list
urlpatterns = [
    path ('register/',register_courses,name='register_courses'),
    path('list/',course_list,name="course_list"),
    path('profile/<int:id>/',course_profile,name="course_profile"),
    path('edit/<int:id>/',edit_course,name="edit_course"),
    path('delete/<int:id>/',delete_courses,name="delete_courses"),




]