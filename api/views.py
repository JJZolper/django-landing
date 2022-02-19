from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from api.serializers import *

class CreateUserAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer