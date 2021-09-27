from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=12)
    description=models.TextField(max_length=200)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(max_length=12)
    
    