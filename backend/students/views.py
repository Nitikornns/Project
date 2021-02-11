from rest_framework import viewsets
from .models import Student, Skill, Language, Education, Picture, Work
from .serializers import StudentSerializer, SkillSerializer, LanguageSerializer, EducationSerializer, PictureSerializer, WorkSerializer
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class SkillsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class LanguagesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class EducationsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class PicturesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class WorksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)
