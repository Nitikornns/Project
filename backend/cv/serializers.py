from rest_framework.serializers import ModelSerializer
from .models import Info, Skill, Talent, Language, Education, Picture, Experience, Hobby, Work


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class HobbySerializer(ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class TalentSerializer(ModelSerializer):
    class Meta:
        model = Talent
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


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
