from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.Model.Account import Account, Note, Point

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.Serializers.NoteDetailSerializer import NoteDetailSerializer
from api.Serializers.PointDetailSerializer import PointDetailSerializer
from api.Serializers.NoteGetSerializer import NoteGetSerializer
import json

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletePoint(request,id):
    request_data = request.data
    try:
        serializer = NoteGetSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data["title"])
            noteObject = Note.objects.get(account__user=request.user,title=serializer.validated_data["title"])
            pointObject = Point.objects.get(note=noteObject,id=id)
            pointObject.delete()
            data = {
                "message":"Point deleted",
                "status":status.HTTP_200_OK
            }
            return Response(data,data["status"])
        else:
            data = {
                "message":"Invalid paramters",
                "status":status.HTTP_400_BAD_REQUEST
            }
            return Response(data,data["status"])
    except Point.DoesNotExist as e:
        data = {
            "message": "Point does not exist.",
            "status": status.HTTP_400_BAD_REQUEST,
        }
        return Response(data,data["status"])
    except Note.DoesNotExist as f:
        data = {
            "message": "Note does not exist.",
            "status": status.HTTP_400_BAD_REQUEST,
        }
        return Response(data,data["status"])