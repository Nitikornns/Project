from rest_framework import viewsets
from .models import Hobby, Info, Skill, Talent, Education, Picture, Experience, Hobby, Work
from .serializers import InfoSerializer, SkillSerializer, TalentSerializer, EducationSerializer, PictureSerializer, ExperienceSerializer, HobbySerializer, WorkSerializer
from rest_framework.permissions import IsAuthenticated


class InfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

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


class TalentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)


class HobbiesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

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


class ExperiencesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def perform_create(self, serializer):
        return serializer.save(accountid=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(accountid=self.request.user)
