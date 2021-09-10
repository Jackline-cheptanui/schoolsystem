from django.db import models



# Create your models here.
class Student(models.Model):
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    first_name=models.CharField(max_length=15, null=True)
    last_name=models.CharField(max_length=12, null=True)
    age=models.PositiveSmallIntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    rolenumber=models.CharField(max_length=17, null=True)
    district=models.CharField(max_length=18, null=True)
    gender_choices=(
        ("1",'Male'),
        ("2",'Female'),
        ("3",'Others'),
    )
    gender=models.CharField(max_length=19, choices =gender_choices, null=True)
    email=models.EmailField(max_length=30, null=True)
    student_id=models.PositiveSmallIntegerField(null=True)
    nationality_choices=(
        ('1', 'Kenya'),
         ('2', 'Uganda'),
          ('3', 'Rwanda'),
    )
    nationality=models.CharField(max_length =23,choices=nationality_choices, null=True)
    nationality_id=models.CharField(max_length=20, null=True)
    medical_report=models.FileField(null=True)
    language=models.CharField(max_length=20, null=True)
    laptopserialnumber=models.CharField(max_length=16, null=True)
    date_of_enrollment=models.DateField(null=True)
    profile=models.ImageField(upload_to='images/', null=True)
    phone_number=models.CharField(max_length=15, null=True)
    language_choices=(
        ('1','English'),
        ('2','kiswahili'),
        ('3','kinyaradwa'),
    )
    language=models.CharField(max_length=6, choices =language_choices, null=True)



    
    


