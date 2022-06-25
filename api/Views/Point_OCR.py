from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.Model.Account import Account, Point, Note

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.Serializers.NoteDetailSerializer import NoteDetailSerializer
from api.Serializers.PointDetailSerializer import PointDetailSerializer
from api.Serializers.PointCreateSerializer import PointCreateSerializer
from api.Serializers.CustomPointSerializer import CustomPointSerializer
from api.Serializers.FileSerializer import FileSerializer
import json
import cv2
from PIL import Image
import pytesseract
import base64
from django.db import IntegrityError
import os
import numpy as np


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def get_text_from_image(request):
    # Read image with opencv
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        accountObject = Account.objects.get(username=request.user.username)
        try:
            file = request.data["image"]
            if bool(file) == False:
                raise KeyError
        except KeyError:
            data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Image not uploaded",
            }
            return Response(data)
    # img_path = request.build_absolute_uri(pictureObject.image.url)
    
        img = Image.open(serializer.validated_data["image"]).convert('RGB')
        open_cv_image = np.array(img)
        img = open_cv_image[:, :, ::-1]
        "media/images/testocr.png"
        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to remove some noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        result = pytesseract.image_to_string(image=img)
        try:
            noteObject = Note.objects.create(account=accountObject,title=result[:10])
            noteObject.save()
            pointObject = Point.objects.create(matter=result,note=noteObject).save()
        except IntegrityError as e:
            data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Note already saved."
            }
        
        data = {
            "status": status.HTTP_200_OK,
            "message": "Point saved! \n Found text inside image.",
            "data": result,
        }
        return Response(data)
    else:
        data = {
            "message": "Error in request!",
            "status": status.HTTP_400_BAD_REQUEST,
            "data": serializer.errors,
        }
        return Response(data)
