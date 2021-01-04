from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['userid', 'year', 'name', 'surname', 'idcard',
                  'commencementday', 'email', 'telphoneNumber', 'password']
