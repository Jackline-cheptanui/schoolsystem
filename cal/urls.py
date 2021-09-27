from django.conf.urls import url
from django.urls.conf import path
from . import views
 
 
urlpatterns = [
   url('calendar/', views.CalendarView.as_view(), name='CalenderView'),
   url('forms/', views.event, name='event_form')
]
