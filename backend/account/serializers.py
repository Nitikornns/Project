from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.tokens import RefreshToken


class AccountSerializer(ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = Account(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
