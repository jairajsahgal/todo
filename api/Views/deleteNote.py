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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request,title):
    try:
        noteObject = Note.objects.get(title=title)
        noteObject.delete()
        data = {
            "message":"Note Deleted",
            "status":status.HTTP_200_OK,
        }
        return Response(data,data["status"])
    except Note.DoesNotExist as e:
        data = {
            "message":"Note doesn't exist.",
            "status":status.HTTP_400_BAD_REQUEST
        }
        return Response(data,data["status"])


