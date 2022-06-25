from api.Model.Account import Point
from rest_framework import serializers

class PointDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['matter','created','id']