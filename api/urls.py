
# from schoolsystem.event.models import Event
# from schoolsystem.courses.models import Courses
# from schoolsystem.trainer.models import Trainer
from django.urls.conf import include, path 
from rest_framework import routers

from .views import StudentViewset
from .views import TrainerViewset
from.views import CoursesViewset
from .views import EventViewset


router=routers.DefaultRouter()
router.register(r"student",StudentViewset)
router.register(r"trainer",TrainerViewset)
router.register(r"courses",CoursesViewset)
router.register(r"events",EventViewset)

urlpatterns=[
    path("",include(router.urls)),
    # path('trainer/',Trainer, name='Trainer'),
    # path('courses/',Courses,name='Courses'),
    # path('event/',Event,name='Event'),
]