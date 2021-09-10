from django.conf.urls import url
from . import views
app_name = 'cal'
urlpatterns = [
    url('eventcalendar/', views.CalendarView.as_view(), name='calendar'),
    url("eventform/",views.event, name= "eventform"), 
]


