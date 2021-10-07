from django.test import TestCase
from django import urls
import django
from django.conf.urls import url
from django.http import request
from .models import Trainer
import datetime
from django.urls import reverse



class TrainerModelTestCase(TestCase):
    def setUp(self):
      self.trainer=Trainer(first_name= "AkiraChix",
      last_name="chepsiror",
      gendar="male",
      age=28,
      nationality="kenya",
      language="kiswahili",
      email="Thomas@gmail.com",
      id=2986444,
     trainer_Bio="he is a trainer at AkiraChix.")

    def test_full_name_contain_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    def test_full_name_contain_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())
    def test_register_trainer_view(self):
        url=reverse ("register_trainer")
        data={"first_name":self.trainer.first_name,
              "last_name":self.trainer.last_name,
              "nationality":self.trainer.nationality,}
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)


