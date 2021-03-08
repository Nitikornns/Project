from rest_framework.serializers import ModelSerializer
from .models import Info, Skill, Language, Education, Picture, Work


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
