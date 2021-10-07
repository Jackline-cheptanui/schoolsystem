# from schoolsystem.trainer.views import trainer_profile
from django.db import models


# Create your models here.
class Courses(models.Model):
    def full_name(self):
        return f"{self.course_name}{self.trainer}"
    course_name=models.CharField(max_length=30,null=True)
    trainer=models.CharField(max_length=20,null=True)
    syllabus=models.FileField(upload_to='documents/%y/%m/%d',null=True)
    course_code=models.CharField(max_length=12,null=True)
    coursedescription=models.TextField(null=True)
    profile=models.ImageField(upload_to='images/', null=True)
   