from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    rolenumber=models.CharField(max_length=17)
    district=models.CharField(max_length=18)
    gendar=models.CharField(max_length=6)
    email=models.EmailField(max_length=17)
    Student_id=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=20)
    nationality_id=models.CharField(max_length=20)
    medical_report=models.FileField()
    language=models.CharField(max_length=20)
    laptopserialnumber=models.CharField(max_length=16)
    date_of_enrollment=models.DateField()
    profile=models.ImageField()
    phone_number=models.CharField(max_length=15)


