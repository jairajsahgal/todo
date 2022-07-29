from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from api.Model.Account import Account, Note, Point

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.Serializers.PointDetailSerializer import PointDetailSerializer
import json

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getTodos(request):
    accountObject = Account.objects.get(username=request.user.username)
    notesObject = Note.objects.filter(account__username=accountObject.username)
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
            pointObjects = Point.objects.filter(note=note)
            serializer = PointDetailSerializer(instance=pointObjects,many=True)
            details[note.title]=serializer.data
        data = {
            "message":"Details",
            "status":status.HTTP_200_OK,
            "data":details
        }
        return Response(data,data["status"])