
from django.db import models
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models  import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age","nationality","profile")
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age","nationality")

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("course_name","trainer","course_code")


class CalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('Event_Name',"Event_id","Event_planner")


