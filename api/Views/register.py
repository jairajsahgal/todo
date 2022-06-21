from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.Model.Account import Account
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from api.Serializers.AccountRegister import RegisterAccountSerializer
import json

@api_view(['POST'])
def register(request):
    request_data = request.data
    serializer = RegisterAccountSerializer(data=request_data)
    
    if bool(serializer.is_valid(raise_exception=True)):
        print(serializer.validated_data)
        Account.objects.create(user=serializer.validated_data["user"],username=serializer.validated_data["username"],email=serializer.validated_data["email"]).save()
        data = {
            "message": "Account created!",
            "status": status.HTTP_201_CREATED
        }
        return Response(data)
    else:
        data = {
            "message": "Paramters not given properly!",
            "status": status.HTTP_400_BAD_REQUEST,
            "error": serializer.errors
        }
        return Response(data)
