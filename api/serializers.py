from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email',)