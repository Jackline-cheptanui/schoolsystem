from django.test import TestCase
from django import urls
import django
from django.conf.urls import url
from django.http import request
from .models import Courses
import datetime
from django.urls import reverse






class CoursesModelTestCase(TestCase):
    def setUp(self):
      self.courses=Courses(course_name= "mobile",
      course_code=290,
      trainer="james mwai",
      coursedescription="",
     syllabus="dictionary is a collection of value and keys")

    def test_full_name_contain_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    def test_full_name_contain_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())

    def test_register_course_view(self):
        url=reverse ("register_course")
        data={"first_name":self.trainer.first_name,
              "last_name":self.trainer.last_name,}

        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)










