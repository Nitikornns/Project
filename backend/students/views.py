from rest_framework.viewsets import ModelViewSet

from .models import Student, Skill, Language, Education, Picture, Work
from .serializers import StudentSerializer, SkillSerializer, LanguageSerializer, EducationSerializer, PictureSerializer, WorkSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class LanguagesViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class EducationsViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class PicturesViewSet(ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class WorksViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
