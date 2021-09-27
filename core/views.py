
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models import Event

# Create your views here.
def home(request):
    student=Student.objects.count()
    trainer=Trainer.objects.count()
    courses=Courses.objects.count()
    cal=Event.objects.count()
    data={"students":student, "trainers":trainer,"courses":courses,"event":cal}
    return render(request,"home.html",data)

