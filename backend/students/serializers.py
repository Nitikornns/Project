from rest_framework.serializers import ModelSerializer
from .models import Student, Skill, Language, Education, Picture, Work


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


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['educationid', 'datestart',
                  'dateend', 'studentname', 'name', 'detail']


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ['pictureid', 'studentname', 'picturefile']


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = ['workid', 'studentname', 'name', 'detail']
