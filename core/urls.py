
# from student.models import Student
# from trainer.models import Trainer
# from courses.models import Courses
# from event.models import Event
from django.urls import path
from.views import home

urlpatterns=[
    path('',home, name='home_view'),
    # path('course/', Courses, name='Course'),
    # path('trainer/',Trainer, name='Trainer'),
    # path('student/', Student, name='Student'),
    # path('event/',Event,name='event'),
]




