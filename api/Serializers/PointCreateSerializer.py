from api.Model.Account import Point
from rest_framework import serializers

class PointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['matter']