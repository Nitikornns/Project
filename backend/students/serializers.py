from rest_framework.serializers import ModelSerializer
from .models import Student, Skill, Language


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentcode', 'year', 'name', 'surname', 'idcard',
                  'commencementday', 'email', 'telphoneNumber']


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skillid', 'name',
                  'studentname', 'sumscore', 'score']


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = ['languageid', 'studentname',
                  'name', 'score', 'sumscore']
