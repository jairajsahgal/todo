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

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getTodos(request):
    accountObject = Account.objects.get(username=request.user.username)
    notesObject = Note.objects.filter(account__username=accountObject.username)
    temp=notesObject.exists()
    if not notesObject.exists():
        data = {
            "message": "Empty todos!",
            "status": status.HTTP_400_BAD_REQUEST,
        }
        return Response(data)
    else:
        details = dict()
        for note in notesObject:
            details[note.title]=None
            pointObjects = note.point_set.all()
            serializer = PointDetailSerializer(instance=pointObjects,many=True)
            details[note.title]=serializer.data
    
        return Response(details)