from django.urls import path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('infos', InfoViewSet)
router.register('skills', SkillsViewSet)
router.register('talents', TalentsViewSet)
#router.register('languages', LanguagesViewSet)
router.register('educations', EducationsViewSet)
router.register('pictures', PicturesViewSet)
router.register('experiences', ExperiencesViewSet)
router.register('hobbies', HobbiesViewSet)
router.register('works', WorksViewSet)


urlpatterns = router.urls
