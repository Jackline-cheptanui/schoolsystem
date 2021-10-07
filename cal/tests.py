from django.test import TestCase
from django import urls
import django
from django.conf.urls import url
from django.http import request
from .models import Event
import datetime
from django.urls import reverse





class EventModelTestCase(TestCase):
    def setUp(self):
      self.event=Event(title= "presentation",
      description="presentation of project",
      start_time=7,
      end_time=12,)

    def test_full_time_contain_start_time(self):
        self.assertIn(self.event.start_time,self.event.full_time())
        
    def test_full_time_contain_end_time(self):
        self.assertIn(self.event.end_time,self.event.full_time())

    def test_event_form_view(self):
        url=reverse ("event_form")
        data={"start_time":self.event.start_time,
        "end_time":self.event.end_time,}

        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
