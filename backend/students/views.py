from rest_framework.viewsets import ModelViewSet

from .models import Student, Skill, Language
from .serializers import StudentSerializer, SkillSerializer, LanguageSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class LanguagesViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
