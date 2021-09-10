from typing import ClassVar
from django.db import models
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age")
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age","nationality")

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("course_name","trainer","course_code")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('tittle',"end_time","start_time")


