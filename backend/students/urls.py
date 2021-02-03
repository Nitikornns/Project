from django.urls import path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'students', StudentsViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'languages', LanguagesViewSet)
router.register(r'educations', EducationsViewSet)
router.register(r'pictures', PicturesViewSet)
router.register(r'works', WorksViewSet)


urlpatterns = router.urls
