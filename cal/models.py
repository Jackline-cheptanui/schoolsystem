from django.db import models
import datetime


class Event(models.Model):
    def full_time(self):
        return f"{self.start_time}{self.end_time}"
    title=models.CharField(max_length=12)
    description=models.TextField(max_length=200)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(max_length=12)
    
    