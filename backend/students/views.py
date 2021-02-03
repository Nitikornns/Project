from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student, Skill, Language, Education, Picture, Work
from .serializers import StudentSerializer, SkillSerializer, LanguageSerializer, EducationSerializer, PictureSerializer, WorkSerializer
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class LanguagesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class EducationsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class PicturesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class WorksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
