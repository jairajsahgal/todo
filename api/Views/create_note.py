from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.Model.Account import Account, Note, Point

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.Serializers.NoteDetailSerializer import NoteDetailSerializer
from api.Serializers.PointDetailSerializer import PointDetailSerializer
import json


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request):
    request_data = request.data
    a=Account.objects.get(user=request.user)
    serializer = NoteDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            noteObject = Note.objects.get(account=a,title=serializer.data["title"])
            data = {
                "message": "Note already exists.",
                "status":status.HTTP_400_BAD_REQUEST,
                "data":{
                    "title":noteObject.title
                }
            }
            return Response(data,data["status"])
        except Note.DoesNotExist:
            Note.objects.create(account=a,title=serializer.data["title"])
            data = {
                "message": "Note created!",
                "status": status.HTTP_201_CREATED,
            }
            return Response(data)
    else:
        data = {
            "message":"Invalid Parameters",
            "status":status.HTTP_400_BAD_REQUEST,
        }
        return Response(data,data["status"])

