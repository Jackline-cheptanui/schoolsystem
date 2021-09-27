from django.db import models
# from django.db.models.enums import Choices

# Create your models here.
class Trainer(models.Model):
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=12,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    course_Name=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=17,null=True)
    contract=models.FileField(null=True)
    cource=models.CharField(max_length=12,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    trainer_Bio=models.TextField(null=True)
    language=models.CharField(max_length=3,null=True)
    id=models.CharField(primary_key=True,max_length=18)
    profile=models.FileField(upload_to='images/' ,null=True)
    gendar_choices=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others'),
    )
    gendar=models.CharField(max_length=19, choices =gendar_choices,null=True)
    nationality_choices=(
        (u'K', 'Kenya'),
         (u'U', 'Uganda'),
          (u'R', 'Rwanda'),
    )
    nationality=models.CharField(max_length =23,choices=nationality_choices,null=True)
    language_choices=(
        (u'E','u''English'),
        (u'k','u''kiswahili'),
        (u'ki','u''kinywaranda'),
    )
    language=models.CharField(max_length=6, choices =language_choices,null=True)
    
    
    
