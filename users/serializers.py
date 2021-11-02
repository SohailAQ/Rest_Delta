from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers

from users.models import CustomUser


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'profile', 'dob', 'date_joined', 'last_login')
        read_only_fields = ('id', 'email', 'date_joined', 'last_login',)


class LoginSerializer(RestAuthLoginSerializer):
    username = None
