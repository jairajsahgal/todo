from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    image = serializers.ImageField()
    class Meta:
        fields = ['image']
    