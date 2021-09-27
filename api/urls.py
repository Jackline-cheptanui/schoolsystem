
from django.urls.conf import include, path 
from rest_framework import routers

from .views import StudentViewset
from .views import TrainerViewset
from.views import CoursesViewset
from .views import CalViewset


router=routers.DefaultRouter()
router.register(r"student",StudentViewset)
router.register(r"trainer",TrainerViewset)
router.register(r"courses",CoursesViewset)
router.register(r"cal",CalViewset)

urlpatterns=[
    path("",include(router.urls)),
    # path('trainer/',Trainer, name='Trainer'),
    # path('courses/',Courses,name='Courses'),
    # path('event/',Event,name='Event'),
]