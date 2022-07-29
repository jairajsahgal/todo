from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.Model.Account import Account, Note, Point

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.Serializers.NoteDetailSerializer import NoteDetailSerializer
from api.Serializers.PointDetailSerializer import PointDetailSerializer
from api.Serializers.PointCreateSerializer import PointCreateSerializer
from api.Serializers.CustomPointSerializer import CustomPointSerializer
import json


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_point(request):
    request_data = request.data
    serializer = CustomPointSerializer(data=request_data)
    if serializer.is_valid():
        note = Note.objects.filter(account__user=request.user,title=request_data["title"])
        if note.exists():
            serializer = PointCreateSerializer(data=request_data)
            if serializer.is_valid(raise_exception=True):
                Point.objects.create(note=note[0],matter=serializer.validated_data["matter"]).save()
                data = {
                    "message": "Point saved!",
                    "status": status.HTTP_200_OK,
                }
                return Response(data)
            else:
                data = {
                    "message": "Invalid paramters",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
                return Response(data)
        else:
            data = {
                "message": "Note doesn't exist.",
                "status": status.HTTP_400_BAD_REQUEST,
            }
            return Response(data)
    else:
        data = {
            "message":"Proper parameters not given!",
            "status":status.HTTP_400_BAD_REQUEST
        }
        return Response(data)


