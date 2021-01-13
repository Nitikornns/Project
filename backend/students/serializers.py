from rest_framework.serializers import ModelSerializer
from .models import Student, Skill


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentcode', 'year', 'name', 'surname', 'idcard',
                  'commencementday', 'email', 'telphoneNumber']


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skillid', 'studentname', 'languagename', 'score']
