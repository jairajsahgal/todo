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
from django.contrib.auth import login
from api.Serializers.AccountRegister import RegisterAccountSerializer
import json


@api_view(['POST'])
def login_api(request):
    request_data = request.data
    serializer = AuthTokenSerializer(data=request_data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    accountObject = Account.objects.get(username=user.username)
    token = AuthToken.objects.create(user)[1]
    data = {
        "message": "Authenticated!",
        "details": {
            "username":accountObject.username,
            "email":accountObject.email,
        },
        "token": token,
        
    }
    return Response(data)