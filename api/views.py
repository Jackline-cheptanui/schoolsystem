
from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models import Event
from .serializers import StudentSerializer
from.serializers import TrainerSerializer
from.serializers import CoursesSerializer
from .serializers import EventSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class= StudentSerializer

class TrainerViewset(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CoursesViewset(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serialzer_class=EventSerializer


