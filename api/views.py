from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from api.serializers import *
from api.services import *

def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            ip_loc = user_ip_location(request)
            serializer.save(ip_address=ip_loc['ip_address'], us_state=ip_loc['us_state'], country=ip_loc['country'])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)