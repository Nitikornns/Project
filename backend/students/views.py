from rest_framework.viewsets import ModelViewSet

from .models import Student, Skill
from .serializers import StudentSerializer, SkillSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
