
from django import forms
from django.forms import fields
from django.db import models
from .models import Student
class StudentRegistrationForms(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"