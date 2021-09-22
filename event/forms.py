
from django import forms

from .models import Event
class EventRegistrationForms(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"




# from django.db import models
# from django.forms import ModelForm, DateInput
# from django.forms.widgets import Textarea
# from .models import Event
# class EventForm(ModelForm):
#     class Meta:
#         model=Event
#         WidgetS = {
#          'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
#          'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#          'description':Textarea(attrs={'class':'form_control','id':'des'}),
#         }
#         fields= '__all__'
#     def __init__ (Self, *args, **kwargs) :
#         super(EventForm, Self). __init__(*args, **kwargs)
#         Self.fields["start_time"].input_formats=('%Y-%m-%dT%H:%M',)
#         Self.fields["end_time"].input_formats=('%Y-%m-%dT%H:%M',)

